from workalendar.registry import registry
from workalendar.core import CoreCalendar

from datetime import date, timedelta

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def proc_holidays():
    calendars = registry.get_calendars()
    for k, v in calendars.items():
        cal = v()
        ical_content = cal.export_to_ical(period=[2020,2023])
        with open(f'./holidays-ics/{k}.ics', 'w') as f:
            f.write(ical_content)

def proc_workingdays():
    calendars = registry.get_calendars()
    start_date = date(2020, 1, 1)
    end_date = date(2024, 1, 1)
    for k,v in calendars.items():
        cal: CoreCalendar = v()
        # iterate through all dates 
        res = []
        for single_date in daterange(start_date, end_date):
            if not cal.is_working_day(single_date):
                res.append(single_date)
        with open(f'./workingdays/{k}.txt', 'w') as f:
            f.write('\n'.join([x.strftime("%Y-%m-%d") for x in res]))

def main():
    proc_holidays()
    proc_workingdays()

main()
