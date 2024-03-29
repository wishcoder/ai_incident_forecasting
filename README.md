# AI Incident Forecasting
Transform textual and categorical data into numerical formats that ML models can process. For instance, issue types, system components affected, and steps taken can be encoded using techniques like one-hot encoding, TF-IDF for text, or embedding layers for more complex representations.

## Data Source

* Code Repositories
* Bug Tracking System
* Incident Management System
* System of Record Tool
* Wiki Pages
 
## System of Record

| Component Type | Component Name | app_id      | component_id      |
|----------------|----------------|-------------|-------------------|
| Router         | Router-1       | router_1    | router_1_comp     |
| Router         | Router-2       | router_2    | router_2_comp     |
| Firewall       | Firewall-1     | firewall_1  | firewall_1_comp   |
| Firewall       | Firewall-2     | firewall_2  | firewall_2_comp   |
| Application    | App-1          | app_1       | app_1_comp        |
| Application    | App-2          | app_2       | app_2_comp        |
| Application    | App-3          | app_3       | app_3_comp        |
| Application    | App-4          | app_4       | app_4_comp        |
| Service        | Service-1      | service_1   | service_1_comp    |
| Service        | Service-2      | service_2   | service_2_comp    |
| Service        | Service-3      | service_3   | service_3_comp    |
| Service        | Service-4      | service_4   | service_4_comp    |
| Database       | Database-1     | db_1        | db_1_comp         |

## System of Record - Details

### Applications
* App-1 (app_id=app_1, component_id=app_1_comp)
* App-2 (app_id=app_2, component_id=app_2_comp)
* App-3 (app_id=app_3, component_id=app_3_comp)
* App-4 (app_id=app_4, component_id=app_4_comp)

### Services
* Service-1 (app_id=service_1, component_id=service_1_comp)
* Service-2 (app_id=service_2, component_id=service_2_comp)
* Service-3 (app_id=service_3, component_id=service_3_comp)
* Service-4 (app_id=service_4, component_id=service_4_comp)

### Databases
* Databse-1 (app_id=db_1, component_id=db_1_comp)

### Routers
* Router-1 (app_id=router_1, component_id=router_1_comp)
* Router-2 (app_id=router_2, component_id=router_2_comp)

### Firewalls
* Firewall-1 (app_id=firewall_1, component_id=firewall_1_comp)
* Firewall-2 (app_id=firewall_2, component_id=firewall_2_comp)


## Network Diagram

```
       +--------------------------------------------+
       |               Outside Network              |
       +--------------------------------------------+
           |                                   |
           v                                   v
  +--------+--------+                  +--------+--------+  
  |   Router-1      |                  |   Router-2      |
  +--------+--------+                  +--------+--------+
           |                                   |
           v                                   v
  +--------+--------+                  +--------+--------+
  |   Firewall-1    |                  |   Firewall-2    |
  +--------+--------+                  +--------+--------+
           |                                   |
           v                                   v
  +--+--+  +--+--+                     +--+--+  +--+--+
  |App-1|  |App-2|                     |App-3|  |App-4|
  +--+--+  +--+--+                     +--+--+  +--+--+
     |       |                            |       |
     +-------+                            +-------+
         |                                    |
         v                                    v
     +----+----+                         +----+----+
     |Service-1|                         |Service-3|
     +----+----+                         +----+----+
          |                                   |
          v                                   v
     +----+----+                         +----+----+
     |Service-2|                         |Service-4|
     +----+----+                         +----+----+
           |                                   |
           +-----------+-----+-----+-----------+
                             |
                             v
                       +-----+-----+
                       | Database-1|
                       +-----------+
```

## Architecture Flow


**1.** Outside Network wants to connect to App-1 or App-2 will have to go through Router-1. Router-1 connects to Firewall-1. Based on the request Firewall-1 sends the request to App-1 or App-2 .

**2.** Outside Network wants to connect to App-3 or App-4 will have to go through Router-2. Router-2 connects to Firewall-2. Based on the request Firewall-2 sends the request to App-3 or App-4 .

**3.** App-1 connects to Service-1. Service-1 connects Service-2. Service-2 connects to to database-1 and read data.

**4.** App-2 connects to Service-1. Service-1 connects Service-2. Service-2 connects to to database-1 and read data.

**5.** App-3 connects to Service-3. Service-3 connects Service-4. Service-4 connects to to database-1 and read data.

**6.** App-4 connects to Service-3. Service-3 connects Service-4. Service-4 connects to to database-1 and read data.

## Incident Template

> ```
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <meta name="viewport" content="width=device-width, initial-scale=1.0">
>     <title>Incident Report: [Incident Title]</title>
>     <style>
>         .incident-report { font-family: Arial, sans-serif; }
>         .incident-section { margin-bottom: 20px; }
>         .incident-title { color: #333; }
>         .incident-detail, .incident-description, .impact-analysis, .resolution-steps, .incident-status, .lessons-learned { color: #666; }
>         .detail-label { font-weight: bold; }
>         .detail-info { margin-left: 5px; }
>     </style>
> </head>
> <body>
>     <article class="incident-report">
>         <h1 class="incident-title">Incident Report</h1>
>         <section class="incident-section incident-detail">
>             <h2>Incident Details</h2>
>             <p><span class="detail-label">Incident ID:</span><span class="detail-info">[Unique Incident ID]</span></p>
>             <p><span class="detail-label">Title:</span><span class="detail-info">[Incident Title]</span></p>
>             <p><span class="detail-label">Date and Time:</span><span class="detail-info">[Date and Time of Incident]</span></p>
>             <p><span class="detail-label">Reported By:</span><span class="detail-info">[Reporter Name/Department]</span></p>
>             <p><span class="detail-label">Component Affected:</span><span class="detail-info">[Affected Component]</span></p>
>         </section>
>         <section class="incident-section incident-description">
>             <h2>Incident Description</h2>
>             <p>[Detailed Description of the Incident]</p>
>         </section>
>         <section class="incident-section impact-analysis">
>             <h2>Impact Analysis</h2>
>             <p>[Analysis of the Incident's Impact]</p>
>         </section>
>         <section class="incident-section resolution-steps">
>             <h2>Resolution Steps</h2>
>             <p>[Step-by-Step Resolution]</p>
>             <p><span class="detail-label">Resolved By:</span><span class="detail-info">[Name/Team]</span></p>
>             <p><span class="detail-label">Resolution Date and Time:</span><span class="detail-info">[Date and Time of Resolution]</span></p>
>         </section>
>         <section class="incident-section incident-status">
>             <h2>Status</h2>
>             <p>[Current Status of the Incident]</p>
>         </section>
>         <section class="incident-section lessons-learned">
>             <h2>Lessons Learned</h2>
>             <p>[Insights or Lessons Learned from the Incident]</p>
>         </section>
>     </article>
> </body>
> </html>
> ```


## List of incidents, impacts, and resolutions

```
1)
> Incident: Database-1 is not accessible
> Impact: Service-2 and Service-4 are not able to access data. As a result Service-1 and Service-3 is not able to provide data to App-1, App-2 and App-3 and App-4
> Resolutions: Restart Database-1

2) 
> Incident: Router-1 is not reachable
> Impact: Outside world is not able to access App-1 and App-2
> Resolutions: Restart Router-1

3) 
> Incident: Router-1 configuration changes
> Impact: Outside world is not able to access App-1 and App-2
> Resolutions: Roll back Router-1 configuration changes

4) 
> Incident: Router-2 is not reachable
> Impact: Outside world is not able to access App-3 and App-4
> Resolutions: Restart Router-2

5) 
> Incident: Router-2 configuration changes
> Impact: Outside world is not able to access App-3 and App-4
> Resolutions: Roll back Router-2 configuration changes

6) 
> Incident: Firewall-1 is not reachable
> Impact: Outside world is not able to access App-1 and App-2
> Resolutions: Restart Firewall-1

7) 
> Incident: Firewall-1 configuration changes
> Impact: Outside world is not able to access App-1 and App-2
> Resolutions: Roll back Firewall-1 configuration changes

8) 
> Incident: Firewall-1 configuration change routing all traffic to App-1
> Impact: Outside world is not able to access App-2
> Resolutions: Roll back Firewall-1 configuration changes

9) 
> Incident: Firewall-1 configuration change routing all traffic to App-2
> Impact: Outside world is not able to access App-1
> Resolutions: Roll back Firewall-1 configuration changes

10) 
> Incident: Firewall-2 is not reachable
> Impact: Outside world is not able to access App-3 and App-4
> Resolutions: Restart Firewall-2

11) 
> Incident: Firewall-2 configuration changes
> Impact: Outside world is not able to access App-3 and App-4
> Resolutions: Roll back Firewall-2 configuration changes

12) 
> Incident: Firewall-2 configuration change routing all traffic to App-3
> Impact: Outside world is not able to access App-4
> Resolutions: Roll back Firewall-2 configuration changes

13) 
> Incident: Firewall-2 configuration change routing all traffic to App-4
> Impact: Outside world is not able to access App-3
> Resolutions: Roll back Firewall-2 configuration changes

14) 
> Incident: Service-2 is not accessible
> Impact: Service-1 is not able to access Service-2 and not able to provide data back to App-1 and App-2
> Resolutions: Restart Service-2

15) 
> Incident: Service-2 changes
> Impact: Service-1 is able to access Service-2 but due to misconfiguration is not able to provide data back to App-1 and App-2
> Resolutions: Roll back Service-2 changes and restart Service-2

16) 
> Incident: Service-4 is not accessible
> Impact: Service-3 is not able to access Service-4 and not able to provide data back to App-3 and App-4
> Resolutions: Restart Service-4

17) 
> Incident: Service-4 changes
> Impact: Service-3 is able to access Service-4 but due to misconfiguration is not able to provide data back to App-3 and App-4
> Resolutions: Roll back Service-4 changes and restart Service-4

18) 
> Incident: Service-1 is not accessible
> Impact: App-1 and App-2 is not able to access data from Service-1
> Resolutions: Restart Service-1

19) 
> Incident: Service-1 changes
> Impact: App-1 and App-2 is able to access Service-1 but due to misconfiguration is not able to access data
> Resolutions: Roll back Service-1 changes and restart Service-1

20) 
> Incident: Service-3 is not accessible
> Impact: App-3 and App-4 is not able to access data from Service-3
> Resolutions: Restart Service-3

21) 
> Incident: Service-3 changes
> Impact: App-3 and App-4 are able to access Service-3 but due to misconfiguration is not able to access data
> Resolutions: Roll back Service-3 changes and restart Service-3

22) 
> Incident: App-1 is not accessible
> Impact: Outside world is not able to access App-1
> Resolutions: Restart App-1

23) 
> Incident: App-2 is not accessible
> Impact: Outside world is not able to access App-2
> Resolutions: Restart App-2

24) 
> Incident: App-3 is not accessible
> Impact: Outside world is not able to access App-3
> Resolutions: Restart App-3

25) 
> Incident: App-4 is not accessible
> Impact: Outside world is not able to access App-4
> Resolutions: Restart App-4

26) 
> Incident: App-1 configuration changes
> Impact: Outside world is able to access App-1 but due to misconfiguration is not able to use it
> Resolutions: Revert back App-1 configuration changes and restart App-1

27) 
> Incident: App-2 configuration changes
> Impact: Outside world is able to access App-2 but due to misconfiguration is not able to use it
> Resolutions: Revert back App-2 configuration changes and restart App-2

28) 
> Incident: App-3 configuration changes
> Impact: Outside world is able to access App-3 but due to misconfiguration is not able to use it
> Resolutions: Revert back App-3 configuration changes and restart App-3

29) 
> Incident: App-4 configuration changes
> Impact: Outside world is able to access App-4 but due to misconfiguration is not able to use it
> Resolutions: Revert back App-4 configuration changes and restart App-4
```
