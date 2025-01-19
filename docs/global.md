# Pico Global Documentation

Pico Global uses Azure's Traffic Manager for handling global DNS routing.

The process is as follows:

1. Login to Azure and go to `Traffic Manager Profiles`.
2. Create a policy. Name it as you like.
3. Set routing method as desired. We will utilize `Performance` to have Azure auto select based on latency.
4. Select or create a resource group for this profile.

Once the profile is created, we can add instances to load balance between.

1. Click into the policy created above from the profiles page.
2. Under the `Settings` item in the left side bar, click `Endpoints`.
3. Click `Add`. Set the type (`External` most likely). Name as desired. Enter the hostname for the endpoint.
4. Select enable health checks

Then create a CNAME to the traffic manager dns entry and you're all set!
