# ... (previous code remains the same)

class GeoIP:
    # ... (previous code remains the same)

    def is_private_ip(self, ip_address):
        """
        Checks if an IP address is a private IP address (e.g., 192.168.x.x, 10.x.x.x, 172.16.x.x to 172.31.x.x).

        Args:
            ip_address (str): The IP address to check.

        Returns:
            bool: True if the IP address is private, False otherwise.
        """
        parts = ip_address.split('.')
        return len(parts) == 4 and parts[0] in ('10', '192', '172') and (parts[0] == '10' or (16 <= int(parts[1]) <= 31))

    def lookup(self, ip_address):
        # ... (previous code remains the same)

        if self.is_private_ip(ip_address):
            results = OrderedDict([
                ("ip_address", ip_address),
                ("asn", None),
                ("organization", None),
                ("location_string", None),
                ("city", None),
                ("subdivision", None),
                ("country", None),
                ("subdivision_iso", None),
                ("country_iso", None),
                ("latitude", None),
                ("longitude", None)
            ])
        else:
            results = OrderedDict([
                ("ip_address", ip_address),
                ("asn", asn),
                ("organization", organization),
                ("location_string", location_string),
                ("city", city),
                ("subdivision", subdivision),
                ("country", country),
                ("subdivision_iso", subdivision_iso),
                ("country_iso", country_iso),
                ("latitude", latitude),
                ("longitude", longitude)
            ])

        return results

# ... (previous code remains the same)

def process_ip_addresses(input_file, output_file, database_directory=None):
    geoip = GeoIP(database_directory)
    output_data = []
    
    with open(input_file, "r") as infile:
        for line in infile:
            ip_address = line.strip()
            if ip_address:
                result = geoip.lookup(ip_address)
                output_data.append(result)

    with open(output_file, "w") as outfile:
        if output_file.endswith(".csv"):
            csvwriter = csv.DictWriter(outfile, fieldnames=output_data[0].keys())
            csvwriter.writeheader()
            csvwriter.writerows(output_data)
        else:  # Assuming JSON format if not CSV
            json.dump(output_data, outfile, ensure_ascii=False, indent=2)

# ... (previous code remains the same)

if __name__ == "__main__":
    _main()
