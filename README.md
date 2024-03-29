# AI Incident Forecasting
Transform textual and categorical data into numerical formats that ML models can process. For instance, issue types, system components affected, and steps taken can be encoded using techniques like one-hot encoding, TF-IDF for text, or embedding layers for more complex representations.

## Data Source

* Code Repositories
* Bug Tracking System
* Incident Management System
* System of Record Tool
* Wiki Pages
 
# System of Record

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

# Network Diagram

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

# Incident Template

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
</html>

```

