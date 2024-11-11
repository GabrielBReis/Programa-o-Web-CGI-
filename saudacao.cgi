#!/bin/bash

echo "Content-Type: text/html"
echo ""
read -r input
nome=$(echo "$input" | sed 's/^nome=//' | sed 's/+/ /g' | xargs -0 printf '%b\n')

echo "<!DOCTYPE html>"
echo "<html lang=\"pt-br\">"
echo "<head>"
echo "    <meta charset=\"UTF-8\">"
echo "    <title>Saudação</title>"
echo "</head>"
echo "<body>"
echo "    <h2>Olá, $nome!</h2>"
echo "    <p>Seja bem-vindo(a)!</p>"
echo "</body>"
echo "</html>"
