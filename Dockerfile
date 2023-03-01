FROM tiagosamaha/python-firefox

WORKDIR /home/task

COPY . ./

RUN apt update && apt install -y ffmpeg && pip install -r requirements.txt 

CMD (cd src/ && python3 application.py &) && (python3 checker.py 127.0.0.1 8080 check)