FROM python:3.10

EXPOSE 8000/tcp

COPY query-requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip==23.0.1 setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r query-requirements.txt

COPY . .

WORKDIR "/src"

CMD [ "uvicorn", "query_data.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

