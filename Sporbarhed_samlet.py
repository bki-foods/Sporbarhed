#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import Sporbarhed_råkaffe
import Sporbarhed_færdigkaffe
import Sporbarhed_opspræt
import Sporbarhed_shared_functions as ssf


# =============================================================================
# Variables for query connections
# =============================================================================
con_ds = ssf.get_connection('bki_datastore')

# =============================================================================
# Read data from request
# =============================================================================
query_ds_request =  """ SELECT TOP 1 [Id] ,[Forespørgselstype],[Rapport_modtager]
                    ,[Referencenummer] ,[Note_forespørgsel] ,[Modtagelse]  ,[Ordrerelationstype]
                    FROM [trc].[Sporbarhed_forespørgsel]
                    WHERE [Forespørgsel_igangsat] IS NULL """
df_request = pd.read_sql(query_ds_request, con_ds)

# Exit script if no request data is found
if len(df_request) == 0:
    quit()

# =============================================================================
# Set request variables
# =============================================================================
req_type = df_request.loc[0, 'Forespørgselstype']
req_id = df_request.loc[0, 'Id']

# =============================================================================
# Execute correct script
# =============================================================================

if req_type == 0:
    Sporbarhed_færdigkaffe.initiate_report(req_id)
elif req_type == 1:
    Sporbarhed_råkaffe.initiate_report(req_id)
elif req_type == 2:
    pass
    # Sporbarhed_opspræt.initiate_report(req_id)

# Exit script
quit()
