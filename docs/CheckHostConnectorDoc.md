## About the connector

Check host offers various network-related tools and services. It also provides tools for checking the availability and
response time of a website or server from different locations around the world.
<p>This document provides information about the Check Host Connector, which facilitates automated interactions, with a Check Host server using FortiSOAR&trade; playbooks. Add the Check Host Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Check Host.</p>

### Version information

Connector Version: 1.0.0

Authored By: spryIQ.co

Contributors: Jitesh Rathod

Certified: No

## Installing the connector

<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-check-host`

## Prerequisites to configuring the connector

- You must have the URL of Check Host server to which you will connect and perform automated operations and credentials
  to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Check Host server.

## Minimum Permissions Required

- N/A

## Configuring the connector

For the procedure to configure a connector,
click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)

### Configuration parameters

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Check Host</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the URL of the check host server to connect and perform automated operations.<br>
</tbody></table>

## Actions supported by the connector

The following automated operations can be included in playbooks and you can also use the annotations to access
operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Ping Check<br></td><td>Ping Check allows to test the reachability of a host, to measure network latency and packets loss from different servers in the world.<br></td><td>ping_check <br/>Investigation<br></td></tr>
<tr><td>HTTP Check<br></td><td>HTTP is for checking website's response performance and availability from many countries and datacenters.<br></td><td>http_check <br/>Investigation<br></td></tr>
<tr><td>TCP Connection Check<br></td><td>TCP connection checks the possibility of a TCP connection to host's specified port.<br></td><td>tcp_check <br/>Investigation<br></td></tr>
<tr><td>DNS Address Check<br></td><td>DNS is for retrieving A, AAAA and PTR records with TTL (time-to-live) from nameservers around the world for checking updates on DNS servers.<br></td><td>dns_check <br/>Investigation<br></td></tr>
<tr><td>Check Result By Request ID<br></td><td>Retrieve result of a query based on Request ID.<br></td><td>check_result_by_request_id <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Ping Check

#### Input parameters

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Host<br></td><td>Specify the host.<br>
</td></tr><tr><td>Max Nodes<br></td><td>Enter Maximum Node Count.<br>
</td></tr></tbody></table>

#### Output

The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "us1.node.check-host.net": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        []
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ch1.node.check-host.net": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        []
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "pt1.node.check-host.net": null
</code><code><br>}</code>

### operation: HTTP Check

#### Input parameters

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Host<br></td><td>Specify the host.<br>
</td></tr><tr><td>Max Nodes<br></td><td>Enter Maximum Node Count.<br>
</td></tr></tbody></table>

#### Output

The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ok": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "request_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "permanent_link": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "nodes": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "us1.node.check-host.net": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ch1.node.check-host.net": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "pt1.node.check-host.net": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp; }
</code><code><br>}</code>

### operation: TCP Connection Check

#### Input parameters

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Host<br></td><td>Specify the host.<br>
</td></tr><tr><td>Max Nodes<br></td><td>Enter Maximum Node Count.<br>
</td></tr></tbody></table>

#### Output

The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ok": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "request_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "permanent_link": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "nodes": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "us1.node.check-host.net": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ch1.node.check-host.net": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "pt1.node.check-host.net": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp; }
</code><code><br>}</code>

### operation: DNS Address Check

#### Input parameters

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Host<br></td><td>Specify the host.<br>
</td></tr><tr><td>Max Nodes<br></td><td>Enter Maximum Node Count.<br>
</td></tr></tbody></table>

#### Output

The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ok": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "request_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "permanent_link": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "nodes": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "us1.node.check-host.net": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ch1.node.check-host.net": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "pt1.node.check-host.net": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp; }
</code><code><br>}</code>

### operation: Check Result By Request ID

#### Input parameters

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Request ID<br></td><td>Specify the request id.<br>
</td></tr></tbody></table>

#### Output

The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "nodes": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "us1.node.check-host.net": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ch1.node.check-host.net": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "pt1.node.check-host.net": []
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp; }
</code><code><br>}</code>

## Included playbooks

The `Sample - check-host - 1.0.0` playbook collection comes bundled with the Check Host connector. These playbooks
contain steps using which you can perform all supported actions. You can see bundled playbooks in the **
Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Check Host connector.

- Ping Check
- HTTP Check
- TCP Connection Check
- DNS Address Check
- Check Result By Request ID

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those
playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector
upgrade and delete.
