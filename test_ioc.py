from core.ioc import scan_iocs

result = scan_iocs("samples")

print("=" * 50)
print("IOC Scan Report")
print("=" * 50)

for key, value in result.items():
    print(f"{key}: {value}")
    
    