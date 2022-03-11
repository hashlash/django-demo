# example-drf-schema-bug
An example project for demonstrating DRF's schema bug when using SafeString as help_text.

## Bug description

- Create a model with Django's `SafeString` as its help_text.
- Follow the DRF's doc about
  [Generating a dynamic schema with SchemaView](https://www.django-rest-framework.org/api-guide/schemas/#generating-a-dynamic-schema-with-schemaview)
  and [A minimal example with Swagger UI](https://www.django-rest-framework.org/topics/documenting-your-api/#a-minimal-example-with-swagger-ui).
- Swagger UI fails to render the generated schema.

More details on [the discussion](https://github.com/encode/django-rest-framework/discussions/8402).
