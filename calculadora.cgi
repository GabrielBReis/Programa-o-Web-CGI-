#!/bin/bash

echo "Content-Type: text/html"
echo ""
read -r input
echo "<h2>Dados recebidos:</h2>"

num1=$(echo "$input" | sed -n 's/.*num1=\([^&]*\).*/\1/p' | sed 's/+/ /g' | xargs -0 printf '%b\n')
num2=$(echo "$input" | sed -n 's/.*num2=\([^&]*\).*/\1/p' | sed 's/+/ /g' | xargs -0 printf '%b\n')
operacao=$(echo "$input" | sed -n 's/.*operacao=\([^&]*\).*/\1/p' | sed 's/+/ /g' | xargs -0 printf '%b\n')
echo "<p>num1 = $num1</p>"
echo "<p>num2 = $num2</p>"
echo "<p>Operação = $operacao</p>"

if ! [[ "$num1" =~ ^-?[0-9]+(\.[0-9]+)?$ ]] || ! [[ "$num2" =~ ^-?[0-9]+(\.[0-9]+)?$ ]]; then
    echo "<h2>Erro: Por favor, insira números válidos!</h2>"
    exit 1
fi

case $operacao in
    "adicao")
        resultado=$(($num1 + $num2))
        operacao_nome="Adição"
        operacao_simbolo="+"
        ;;
    "subtracao")
        resultado=$(($num1 - $num2))
        operacao_nome="Subtração"
        operacao_simbolo="-"
        ;;
    "multiplicacao")
        resultado=$(($num1 * $num2))
        operacao_nome="Multiplicação"
        operacao_simbolo="*"
        ;;
    "divisao")
        if [ "$num2" == "0" ]; then
            echo "<h2>Erro: Divisão por zero não é permitida!</h2>"
            exit 1
        fi
        resultado=$(($num1 / $num2))
        operacao_nome="Divisão"
        operacao_simbolo="/"
        ;;
    *)
        echo "<h2>Erro: Operação desconhecida.</h2>"
        exit 1
        ;;
esac

echo "<!DOCTYPE html>"
echo "<html lang=\"pt-br\">"
echo "<head>"
echo "    <meta charset=\"UTF-8\">"
echo "    <title>Resultado</title>"
echo "</head>"
echo "<body>"
echo "    <h2>Resultado da $operacao_nome</h2>"
echo "    <p>$num1 $operacao_simbolo $num2 = $resultado</p>"
echo "    <a href=\"/calculadora.html\">Voltar</a>"
echo "</body>"
