FROM rasa/rasa:latest
WORKDIR /app
COPY . .
USER root
RUN rasa train
CMD ["run", "--model", "models", "--enable-api", "--cors", "*"]
