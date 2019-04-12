from datetime import datetime, timezone
import pytz
import zulip
local_tz = pytz.timezone('Asia/Calcutta')
client = zulip.Client(config_file="~/zuliprc")

def utc_to_local(utc_dt):
    local_dt= utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)

def asLocalTimeString(utc_dt):
    return utc_to_local(utc_dt).strftime('%Y-%m-%d %H:%M:%S.%f %Z%z')

def main():
    print("Enter the UTC time : ")
    UTC_string = "2019-04-12 10:43:39"
    UTC_datetimeObject=datetime.strptime(UTC_string, '%Y-%m-%d %H:%M:%S')
    print("UTC time : ", UTC_datetimeObject)
    print("The Local Time is : ",asLocalTimeString(UTC_datetimeObject))
    all_users = client.get_members()
    users = [x for x in all_users['members'] if x['is_bot']==False ]
    print(users)
main()
