from core.timeline import generate_timeline

timeline = generate_timeline("samples/timeline_test")

print("=" * 60)
print("Timeline Report")
print("=" * 60)

for event in timeline:
    print(f"File Name : {event['File Name']}")
    print(f"Created   : {event['Created']}")
    print(f"Modified  : {event['Modified']}")
    print(f"Accessed  : {event['Accessed']}")
    print("-" * 60)