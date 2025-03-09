FROM python:3.10

EXPOSE 5002/tcp

COPY query-requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r cliente-requirements.txt

COPY . .

WORKDIR "/src"

CMD [ "uvicorn", "cliente.main:app", "--host", "localhost", "--port", "8000", "--reload"]