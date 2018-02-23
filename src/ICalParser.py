from icalendar import Calendar, Event
import requests
import traceback
import io

RETRY_COUNT = 5


def getiCalString(url):
    global RETRY_COUNT
    count = 0
    success = False
    return_string = None
    while count < RETRY_COUNT and not success:
        try:
            count += 1
            response = requests.get(url)
            success = True
            if response.status_code == requests.codes.ok:
                print('success!!')
                with io.BytesIO(b"") as fd:
                    for chunk in response.iter_content(chunk_size=128):
                        fd.write(chunk)
                    return_string = fd.getvalue().decode()
        except ConnectionError:
            print('Connection Error occurred')
            traceback.print_exc()
        except TimeoutError:
            print('Timeout Error occurred')
            traceback.print_exc()
        except requests.RequestException:
            print('Requests exception occurred')
            traceback.print_exc()

    return return_string


def parse_ical_string(ical_str):
    cal = None
    if ical_str is not None:
        cal = Calendar.from_ical(ical_str)

    return cal


def getCalendarObject(links):
    return_obj = []

    if type(links) is list:
        for link in links:
            return_obj.append(extractCalendar(link))
    else:
        return_obj = extractCalendar(links)

    return return_obj


def extractCalendar(link):
    ical_str = getiCalString(link)
    cal_obj = parse_ical_string(ical_str)
    return cal_obj