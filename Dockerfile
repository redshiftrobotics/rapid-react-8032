FROM python:3.8

WORKDIR /home

COPY . .

RUN pip install robotpy
RUN pip install robotpy-rev
RUN pip install robotpy-navx

CMD ["python", "robot/robot.py", "deploy"]