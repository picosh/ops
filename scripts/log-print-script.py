import sys
import json

def main():
    for line in sys.stdin:
        try:
            parsed = json.loads(line)
            msg = parsed["msg"]
            user = ""
            if "user" in parsed:
                user = parsed["user"]
            host = ""
            if "host" in parsed:
                host = parsed["host"]
            url = ""
            if "url" in parsed:
                url = parsed["url"]
            status = ""
            if "status" in parsed:
                status = parsed["status"]
            err = ""
            if "err" in parsed:
                err = parsed["err"]
            print(f"{parsed['time']}\t{parsed['level']}\t{user}\t{parsed['service']}\t{msg}\t{err}\t{status}\t{host}\t{url}")
        except Exception as err:
            print(line)
            print("err parsing json", err)

if __name__ == "__main__":
    main()
