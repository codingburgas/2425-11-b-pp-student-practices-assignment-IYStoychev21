FROM oven/bun:1.2.10

WORKDIR /app

COPY bun.lock package.json ./
RUN bun install

COPY . .

EXPOSE 5173

CMD ["bun", "run", "dev", "--", "--host"]

