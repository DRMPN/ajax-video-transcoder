import logging
import sys

from requests_html import HTMLSession

from src.helpers import random_gen

logging.basicConfig(level=logging.INFO)

if len(sys.argv) != 4:
    print("usage: checker.py [IP] [PORT] [COMMAND]")
    sys.exit(1)

IP = sys.argv[1]
PORT = sys.argv[2]
COMMAND = sys.argv[3]
URL = f"http://{IP}:{PORT}/hello"

logging.info(f"Recieved: IP - {IP}; PORT - {PORT}; COMMAND - {COMMAND}; URL - {URL}")

if COMMAND == "check":
    session = HTMLSession()

    response = session.get(URL)

    username = random_gen()
    password = random_gen()

    script = """
        () => {
                $("#reguser").val("%s");
                $("#regpass1").val("%s");
                $("#regpass2").val("%s");
                $('#makereg').trigger('click');
                return document;
            }
            """ % (
        username,
        password,
        password,
    )

    response = response.html.render(script=script, reload=True, keep_page=True)

    if "danger" in response:
        logging.error("Not registered")
        exit(102)

    # sign in check

    logging.info("OK")
    exit(101)
else:
    logging.info(f"Error: {COMMAND} not found")
    exit(1)
