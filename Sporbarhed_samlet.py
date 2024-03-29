#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import Sporbarhed_råkaffe
import Sporbarhed_færdigkaffe
import Sporbarhed_rework
import Sporbarhed_emballage
import Sporbarhed_shared_functions as ssf
import Sporbarhed_risteordre
import Sporbarhed_shared_server_information as sssi


# =============================================================================
# Read data from request
# =============================================================================
query_ds_request =  """ SELECT TOP 1 [Id] ,[Forespørgselstype],[Rapport_modtager]
                    ,[Referencenummer] ,[Note_forespørgsel] ,[Modtagelse]  ,[Ordrerelationstype]
                    FROM [trc].[Sporbarhed_forespørgsel]
                    WHERE [Forespørgsel_igangsat] IS NULL """
df_request = pd.read_sql(query_ds_request, sssi.con_ds)

# Exit script if no request data is found
ssf.get_exit_check(len(df_request))

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
    Sporbarhed_rework.initiate_report(req_id)
elif req_type == 3:
    pass
elif req_type in [4,5,6]:
    Sporbarhed_emballage.initiate_report(req_id)
elif req_type == 7:
    pass
    Sporbarhed_risteordre.initiate_report(req_id)

# Exit script
ssf.get_exit_check(0)
