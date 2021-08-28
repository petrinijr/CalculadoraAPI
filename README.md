<h1> CalculadoraAPI</h1>
<i>Uma solução complicada e pouco robusta para um problema simples e que não incomodava ninguém.</i>
<h2>Sobre </h2>
O projeto consiste em criar três APIs separadas responsáveis pelo funcionamento de uma mini-calculadora: <br />

<ol>
<li>A primeira é uma página inicial responsável por receber os pedidos de cálculo
(há limites no que pode ser requisitado) e devolver um <i>código</i>: o <i>alphabetic timestamp</i>
do horário de requisição.</li>
<li>A segunda é uma página que propõe acelerar o cálculo de uma requisição (dado o código), caso o usuário
não queira esperar.<br />
#2021-08-27: é melhor não esperar mesmo, pois ainda não foi implementada a rotina
que automaticamente processa essas requisições.</li>
<li>A terceira recebe o código e, se o cálculo foi bem-sucedido, devolve o valor.</li>
</ol>

<H4>Features</H4>
<ul>
<li>As páginas são <i>feias</i>, feitas em HTML5 puro.</li>
<li>As três APIs rodam no <i>localhost</i> em portas diferentes. É necessário declarar
as variáveis: FLASK_APP=run_app_i.py (i=1,2,3 em cada terminal), APP_y_PORT e
APP_y_HOST (y=1,2,3 para cada i). Sugere-se usar todos os APP_y_HOST=127.0.0.1</li>
<li>Dois pseudo-DB usando arquivos .txt. Entradas são dicts ("json") entre consecutivos '#'.</li>
</ul>