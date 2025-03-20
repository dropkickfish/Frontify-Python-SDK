# Setup
## Steps
- Retrieve schema through introspection or Apollo
    - optionally, use the ```remote_schema_url``` and ```remote_schema_headers``` options in the Ariadne config file
- Run gqlg using ```gqlg --schemaFilePath public-beta.graphql  --destDirPath ./queries-mutations --depthLimit 5```
    - The depth limit is set to 5 for the time being. If deeper recursion is required, custom queries should be set up
- Run Ariadne Codegen with ```ariadne-codegen```

## Requirements
- gql-generator 2.0.0 (gqlg) - https://www.npmjs.com/package/gql-generator
- ariadne-codegen 0.13.0 - https://github.com/mirumee/ariadne-codegen

### Ariadne config
```toml
#pyproject.toml
[tool.ariadne-codegen]
queries_path = "queries-mutations"
schema_path = "public-beta.graphql"
target_package_name = "Frontify"
client_name = "FrontifyClient"
client_file_name = "frontifyClient"
```

