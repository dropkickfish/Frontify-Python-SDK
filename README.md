# Unofficial Frontify Python SDK
Not officially endorsed or supported by Frontify.

Bootstrapped with [gql-generator](https://www.npmjs.com/package/gql-generator) to programatically create queries and mutations from a schema, and [ariadne-codegen](https://github.com/mirumee/ariadne-codegen).

The goal is to eventually publish this as a PyPI package, but it works just fine imported as a module for now.

# Usage
## Client
Import and initialise the client as follows:
```python
import os
from frontify.asyncFrontifyClient import AsyncFrontifyClient as FrontifyClient

frontify_access_token = os.getenv('frontify_access_token')
frontifyHeaders = {'Authorization': f"Bearer {frontify_access_token}",
                   'Content-Type': 'application/json',
                   'X-Frontify-Beta': 'enabled'}
frontifyClient = FrontifyClient(url='https://demo.frontify.com/graphql', headers=frontifyHeaders)
```
NB: The generated client is asyncronous by default, and while better for performance, it will mean that the way of working is different to the client exemplified in the Frontify API Example repository.

All examples will follow the usage of the async client, but a synchronous client is also available.

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

## Using a predefined query

Anything listed as a query in the [GraphQL Reference](https://frontify.github.io/graphql-reference/queries/account) can be accessed directly through the client. For example, to query an account:

```python
accountResponse = asyncio.run(frontifyClient.account())
print("Account ID: ", accountResponse.account.id)
```

or to query brands by ID:
```python
brandResponse = asyncio.run(frontifyClient.brand(id=1234))
print(brandResponse.brand.id)
```

Note the use of ```asyncio.run()``` as these functions are asynchronous and must be awaited.

Alternatively, you can run mutiple queries asynchronously as shown:

```python
async def main(client: FrontifyClient):

    # Await the account query
    response = await client.account()
    # Access the response data
    print("Account ID: ", response.account.id)

    # Await the brand query
    response = await client.brand(1234)
    # Access the response data
    print("Brand ID: ", response.brand.id)


# Run the async function
asyncio.run(main(frontifyClient))
```

## Using a predefined mutation

Mutations can accessed in a very similar way from the client class. For example, an asset upload may look something like this:

```python
async def uploadFile(uploadFileInput: UploadFileInput, file_path: str):
    uploadFileResponse = await frontifyClient.uploadFile(uploadFileInput)
    fileId = uploadFileResponse.upload_file.id
    urls = uploadFileResponse.upload_file.urls
    for url in urls:
        uploadChunk(url)
    createAssetInput = CreateAssetInput(
        fileId=fileId,
        title='test',
        description='test',
        projectId='ey...[REDACTED]',
    )
    return await frontifyClient.create_asset(createAssetInput)


asyncio.run(uploadFile(uploadFileInput, 'test.jpg'))
```

## Execute a custom query
If none of the generated queries work or more depth is required, a custom query can be executed as shown in this example for custom metadata fields:

```python
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
response =  asyncio.run(frontifyClient.execute(custom_query, variables=variables))
data = frontifyClient.get_data(response)
print(data)
```

## Notes on synchronous usage
If using `FrontifyClient` it is not necessary to utilise `asyncio` and queries/mutations can be made without awaiting, for example:

### Import
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
### Simple query
```python
accountResponse = frontifyClient.account()
print("Account ID: ", accountResponse.account.id)
```

### Custom query
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