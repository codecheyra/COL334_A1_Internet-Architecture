# COL374/672 Computer Networks: 2023-24 Semester I

## Assignment 1

### Overview
The purpose of this assignment is to familiarize students with essential network tools such as `traceroute`, `nmap`, `wireshark`, `ifconfig`, etc., to gain practical experience with computer networks.

### Preparatory Tasks
1. **ifconfig (ipconfig on Windows)**
   - Provides details about IP address, gateway, network mask, hardware address, DNS server, etc.
   - Tasks:
     - Run the commands with your computer connected to WiFi or via a smartphone hotspot.
     - Check the IP address of your phone when connected via WiFi or 2G/3G/4G networks.

2. **ping**
   - Determines whether a particular IP address is online.
   - Tasks:
     - Send pings with different packet sizes and TTL values.
     - Observe behavior changes across different network interfaces.

3. **traceroute (tracert on Windows)**
   - Displays the sequence of routers a packet traverses to reach a destination.
   - Tasks:
     - Run traceroute for different destinations via various networks.

4. **nslookup**
   - Communicates with DNS servers to get the IP address for a hostname.
   - Tasks:
     - Change the DNS server used and observe differences in responses for popular destinations.

5. **nmap**
   - Discovers hosts online in a network and infers their operating systems.
   - Tasks:
     - Identify devices on your network and determine their OS.

6. **wireshark**
   - Sniffs packets on the wire and presents them in an easily readable format.
   - Tasks:
     - Capture and analyze packet data to understand protocol details.

### Network Configuration Tasks
1. **Configuring IP Address and DNS Server**
   - Tasks:
     - Explore how to configure these settings on Windows, Linux, and Android smartphones.
     - Understand the difference between static and dynamic IP address assignment.

2. **Dynamic IP Assignment Observation**
   - Tasks:
     - Check if the IP address assigned to your smartphone changes over time.
     - Test if communication is possible with a statically assigned IP.

### Network Analysis
1. **Traceroute Analysis**
   - Tasks:
     - Run traceroute for www.iitd.ac.in from home or via a cellular connection.
     - Report any anomalies, such as IPv6 defaults, private IP spaces, and missing routers.

2. **Ping as Traceroute**
   - Tasks:
     - Write a script to replicate traceroute functionality using ping with TTL.

### Internet Architecture
1. **Web Server Traceroutes**
   - Tasks:
     - Perform traceroutes to educational and large content provider web servers from various global locations.
     - Analyze AS-IP lookup results for traffic transitions between ISPs.

2. **Reporting**
   - Tasks:
     - Create a tabular report of hops and latencies between traceroute sources and destinations.
     - Investigate differences in IP addresses resolved from various locations and paths to the same web-server.

### Packet Analysis
1. **Wireshark Packet Capture**
   - Tasks:
     - Capture packets while visiting an HTTP website and analyze DNS, HTTP, and TCP traffic.
     - Report DNS request-response times, the number of HTTP requests, and details of TCP connections.
     - Compare HTTP and HTTPS traffic analysis results.

### Additional Resources
- **Open Traceroute Servers**: [List of Traceroute Servers](#open-traceroute-servers)
- **Public DNS Servers**: [List of Public DNS Servers](#public-dns-servers)

### Open Traceroute Servers
- [Cogentco](http://www.cogentco.com/en/network/looking-glass)
- [Hurricane Electric](http://www.lg.he.net/)
- Additional Servers:
  - [Canada](http://www.tera-byte.com/cgi-bin/nph-trace)
  - [Germany](http://www.han.de/cgi-bin/nph-trace.cgi)
  - [Greece](https://foss.aueb.gr/network_tools/index.php)
  - [Sweden](http://www.macomnet.net/ru/testlab/cgi-bin/nph-trace)
  - [USA](http://www.net.princeton.edu/traceroute.html)

### Public DNS Servers
- Cloudflare: 1.1.1.1
- Verisign: 64.6.64.6
- Open DNS: 208.67.222.222
- AdGuard: 176.103.130.130

For a comprehensive list of public DNS servers and their locations, visit [Public DNS Servers](https://public-dns.info/).
