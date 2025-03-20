# Unofficial Frontify Python SDK
Not officially endorsed or supported by Frontify.

Bootstrapped with [gql-generator](https://www.npmjs.com/package/gql-generator) to programatically create queries and mutations from a schema, and [ariadne-codegen](https://github.com/mirumee/ariadne-codegen).

The goal is to eventually publish this as a PyPI package, but it works just fine imported as a module for now.

# Usage
## Package installation
`pip install install git+https://github.com/dropkickfish/Frontify-Python-SDK/`

## Initializing the client
```python
import os

from dotenv import load_dotenv
from frontify.frontifyClient import FrontifyClient

load_dotenv(verbose=True, override=True)

frontify_access_token = os.getenv('frontify_access_token')
frontifyHeaders = {'Authorization': f"Bearer {frontify_access_token}",
                   'Content-Type': 'application/json',
                   'X-Frontify-Beta': 'enabled'}
frontifyClient = FrontifyClient(url='https://demo.frontify.com/graphql', headers=frontifyHeaders)

```

## Importing types
Import input types from ```frontify.input_types``` to use them for easier creation of query and mutation inputs, for example:
``` python
from frontify.input_types import CreateAssetInput, UploadFileInput

uploadFileInput = UploadFileInput(
    filename='test.jpg',
    size=1000
)

createAssetInput = CreateAssetInput(
    fileId=fileId,
    title='test',
    description='test',
    projectId='ey...[REDACTED]',
)
```

## Simple query
```python
accountResponse = frontifyClient.account()
print("Account ID: ", accountResponse.account.id)
```

## Custom query
```python
# Define a custom query as a string
custom_query = """
query LibraryMetadataFields($libraryId: ID!) {
  library(id: $libraryId) {
    customMetadataProperties {
      ... on CustomMetadataProperty {
        id
        name
        type {
          ... on CustomMetadataPropertyType {
            name
            ... on CustomMetadataPropertyTypeSelect {
              options {
                id
                value
              }
            }
            ... on CustomMetadataPropertyTypeMultiSelect{
              options {
                id
                value
              }
            }
          }
        }
      }
    }
  }
}
"""

# Variables for the query
variables = {"libraryId": 18690}

# Execute the custom query
response =  frontifyClient.execute(custom_query, variables=variables)
data = frontifyClient.get_data(response)
print(data)
```

### Mutation
```python
from frontify.input_types import DeleteAssetInput

deleteAssetInput = DeleteAssetInput(id="12345")
# NB the ID can also be a base64 encoded ID, but must be a string per type rules
deleteResponse = frontifyClient.delete_asset(deleteAssetInput)
print("Delete asset ID: ", deleteResponse.delete_asset.id)
```

## Notes on Beta Functionality
Beta functionality for anything in the public beta schema can be accessed by using the relevant beta headers when initializing the client. 

Beta functionality is curernt as of 19 March 2025.