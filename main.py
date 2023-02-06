from workalendar.registry import registry


def main():
    calendars = registry.get_calendars()
    for k, v in calendars.items():
        cal = v()
        ical_content = cal.export_to_ical(period=[2020,2023])
        with open(f'./ics/{k}.ics', 'w') as f:
            f.write(ical_content)

main()
