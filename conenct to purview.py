from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core import PurviewClient

auth = ServicePrincipalAuthentication(
    tenant_id = "72f988bf-86f1-41af-91ab-2d7cd011db47", 
    client_id = "a5e48d97-b9c6-4eb1-847d-23e7a1ec9030", 
    client_secret = "En_7Q~GdICL1xGTeMXJtZuSbWWeviJyOTkXo_"
)

# Create a client to connect to your service.
client = PurviewClient(
    account_name = "tpcdsdatagovernance",
    authentication = auth
)

from pyapacheatlas.core import AtlasEntity

# Get All Type Defs
all_type_defs = client.get_all_typedefs()

# Get Specific Entities
list_of_entities = client.get_entity(guid=["75fb7fbd-bf11-4c21-b09f-d2f6f6f60000","e4e33041-0aeb-4032-86dc-bc2256c31fcf"])

# Create a new entity
ae = AtlasEntity(
    name = "my table for first python", 
    typeName = "azure_synapse_dedicated_sql_table", 
    qualified_name = "somedb.schema.mytable",
    guid = -10001
)

# Upload that entity with the client
upload_results = client.upload_entities( ae )
