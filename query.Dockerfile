FROM python:3.10

EXPOSE 5002/tcp

COPY query-requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r query-requirements.txt

COPY . .
COPY query_data ./query_data

WORKDIR "/src"

CMD [ "uvicorn", "query_data.main:app", "--host", "localhost", "--port", "8000", "--reload"]