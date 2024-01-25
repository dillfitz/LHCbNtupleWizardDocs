# Monitoring Output

After subitting a request through the Ntuple Wizard, you will be able to monitor your requests on the Open Data Portal.

![Ntupling service](images/Ntupling_service.png)

Clicking the view button associated with a request (the blue button with an eyeball on it) will open an expanded view with details about your request, including the status, status history, and a location to leave comments to communicate with the LHCb open data team. 

![Ntupling service request](images/Ntupling_service_request.png)

The status history will evolve as the request is processed by the open data team, and you will recieve email notifications when the status of the request changes. After the LHCb open data team approves the request, a test production will run over a subset of the data to ensure everything is working properly. This will be indicated in the status history of your request, as seen below.

![Status history 1](images/status_history_1.png)

When the status reads "Awaiting requester confirmation", below the comment section of the expanded view, you will see a heading "Test production results". Some information is delivered back to the user including estimated file sizes and a report of what branches (i.e. variables) will be saved to the Ntuple(s). At this stage, it is up to the user to confirm whether or not the output looks okay. If all looks good, the user can click a button to verify the test production results and initiate processing of the full dataset(s). A preview of the test production output can be viewed by clicking the button shown below.

![Test production preview launch](images/test_production_preview.png)

An example of the test production output, rendered from markdown, will then be displayed on screen. 

![Test production MD1](images/test_production_md_1.png)

![Test production MD1](images/test_production_md_2.png)
