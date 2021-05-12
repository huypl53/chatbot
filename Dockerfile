FROM huypl53/minianaconda3:v2.0

RUN apt update
RUN apt upgrade

RUN https://github.com/phamlehuy53/chatbot.git
COPY chatbot /home/
WORKDIR /home/chatbot

RUN conda create rasa python=3.8.5
RUN conda activate rasa
RUN pip install rasa

CMD ["python", "run_dialouge.py"]
