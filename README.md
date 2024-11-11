# Programa-o-Web-CGI-1 e 2
Programação Web (CGI) 1 e 2 - Atividade de FPS, este é um guia detalhado com uma introdução para cada serviço.

---

## Configuração para Executar Scripts CGI em um Servidor Apache

### Introdução

### Passo a Passo para Configuração

1. **Clone o Repositório**

   Clone o repositório que contém os scripts e arquivos HTML para o seu sistema:

   ```bash
   git clone hhttps://github.com/GabrielBReis/Programa-o-Web-CGI-.git
   cd Programa-o-Web-CGI-
   ```

2. **Instale o Apache**

   Se o Apache não estiver instalado, instale-o com os seguintes comandos:

   ```bash
   sudo apt update
   sudo apt install apache2
   ```

3. **Habilite o Módulo CGI no Apache**

   Para permitir a execução de scripts CGI, habilite o módulo CGI e reinicie o Apache:

   ```bash
   sudo a2enmod cgi
   sudo systemctl restart apache2
   ```

4. **Configure a Pasta `cgi-bin` e Scripts CGI**

   O Apache geralmente executa scripts CGI localizados na pasta `/usr/lib/cgi-bin/`. Copie os scripts CGI clonados para essa pasta e ajuste as permissões:

   ```bash
   sudo cp saudacao.cgi /usr/lib/cgi-bin/
   sudo cp calculadora.cgi /usr/lib/cgi-bin/
   sudo chmod +x /usr/lib/cgi-bin/saudacao.cgi
   sudo chmod +x /usr/lib/cgi-bin/calculadora.cgi
   ```

5. **Configuração de Diretório para CGI no Apache**

   Edite o arquivo de configuração do Apache para garantir que a pasta `/usr/lib/cgi-bin/` permita a execução de scripts CGI. Para isso:

   1. Abra o arquivo de configuração do Apache, geralmente em `/etc/apache2/sites-available/000-default.conf`:

      ```bash
      sudo nano /etc/apache2/sites-available/000-default.conf
      ```

   2. No bloco `<VirtualHost>`, adicione a configuração abaixo para habilitar CGI:

      ```apache
      <Directory "/usr/lib/cgi-bin">
          AllowOverride None
          Options +ExecCGI
          AddHandler cgi-script .cgi .sh
          Require all granted
      </Directory>
      ```

   3. Salve o arquivo e reinicie o Apache:

      ```bash
      sudo systemctl restart apache2
      ```

6. **Coloque as Páginas HTML no Diretório do Servidor Web**

   As páginas HTML precisam estar acessíveis publicamente. Copie `form.html` e `calculadora.html` para a pasta padrão de documentos do Apache:

   ```bash
   sudo cp form.html /var/www/html/
   sudo cp calculadora.html /var/www/html/
   ```

7. **Testando o Funcionamento no Navegador**

   Verifique o funcionamento dos serviços CGI acessando os arquivos HTML no navegador:
   
   - **Saudação**: `http://localhost/form.html`
   - **Calculadora**: `http://localhost/calculadora.html`

---

## Serviço Web CGI 1 - Saudação Personalizada

Este projeto é um exemplo de como criar um serviço web simples utilizando CGI (Common Gateway Interface) com um script Bash para processar dados de um formulário HTML. O objetivo é criar uma página que receba o nome de um usuário através de um formulário HTML e exiba uma mensagem personalizada de saudação.

### Configuração Específica para Saudação Personalizada (CGI 1)

1. **Acesse a Página HTML**

   Acesse o formulário HTML em `form.html`, que coleta o nome do usuário:

   ```plaintext
   http://localhost/form.html
   ```

2. **Preencha o Formulário**

   Insira um nome no campo de entrada e clique em "Enviar". O formulário envia o nome do usuário para o script `saudacao.cgi`, que processa a entrada e exibe uma mensagem de saudação.

3. **Visualize a Saudação**

   Após enviar o formulário, o script CGI responderá com uma página HTML personalizada com uma saudação, como "Olá, [nome_do_usuário]!".


---

## Serviço Web CGI 2 - Calculadora de Operações Básicas

Este projeto ilustra uma aplicação web que realiza operações matemáticas básicas, como adição, subtração, multiplicação e divisão, usando CGI com um script Bash. A interface web permite que o usuário insira dois números, escolha a operação desejada e visualize o resultado da operação em uma página de resposta.

### Configuração Específica para Calculadora de Operações (CGI 2)

1. **Acesse a Página HTML da Calculadora**

   Acesse `calculadora.html`, a interface HTML que permite ao usuário inserir dois números e escolher a operação matemática:

   ```plaintext
   http://localhost/calculadora.html
   ```

2. **Preencha os Campos e Selecione a Operação**

   Insira dois números nos campos de entrada e escolha uma operação (adição, subtração, multiplicação ou divisão) no menu suspenso. Clique no botão "Enviar".

3. **Visualize o Resultado**

   O formulário enviará os dados para o script `calculadora.cgi`, que executará a operação matemática escolhida e exibirá o resultado em uma nova página HTML.

---

### Considerações Finais

- Certifique-se de que os arquivos `saudacao.cgi` e `calculadora.cgi` estejam no diretório `/usr/lib/cgi-bin` e tenham permissão de execução.
- Os arquivos HTML devem estar em `/var/www/html/` para serem acessíveis publicamente.
- Em caso de problemas, verifique o log do Apache para diagnosticar erros:

  ```bash
  sudo tail -f /var/log/apache2/error.log
  ```

Esses passos cobrem toda a configuração necessária para executar os serviços CGI de saudação e calculadora no navegador.