# 25E3_2-TP1

## Exercício 1 Cadastro de Estagiário com Variáveis Simples

Analistas de folha de pagamento de um escritório contábil precisam registrar os dados básicos dos estagiários recém-contratados. O setor de contabilidade trabalha com sistemas automatizados que processam informações individuais como nome, idade e código de departamento para cálculos de benefícios. Para isso, será utilizada uma base fixa com os dados do próprio aluno: [NOME_PROPRIO], [IDADE] e [CODIGO_CLASSE]. O registro inicial desses dados permitirá acionar os módulos de cálculo da jornada, férias e vale-transporte.

Objetivo  
Declarar e armazenar, em um notebook Python, variáveis contendo informações fixas do aluno, que simularão os dados de um novo estagiário no sistema contábil.

Enunciado  
Defina três variáveis: nome_estagiario, idade_estagiario e codigo_departamento. Atribua os valores com o seu nome próprio, idade e código de sua classe, respectivamente. Em seguida, imprima os valores no formato de cadastro de funcionário (um por linha).

## Exercício 2 Simulação de Cliente com Tipos de Dados Primitivos

Uma consultoria em análise de crédito está desenvolvendo um modelo que processa dados simples de clientes: nome, idade, score e status de adimplência. Cada cliente será descrito por variáveis do tipo string, int, float e boolean, com dados simulados. Os testes preliminares usarão os seguintes dados fixos: [NOME_PROPRIO_ALUNO], [IDADE_ALUNO], score 772.4 e status True. Essas definições serão inseridas diretamente no notebook para validar o funcionamento dos tipos básicos no sistema.

Objetivo  
Criar variáveis com diferentes tipos primitivos (string, int, float, boolean) para simular o registro de um cliente e imprimir seus valores e tipos.

Enunciado  
Crie quatro variáveis com os seguintes dados:  
– nome_cliente = '[NOME_PROPRIO]'  
– idade_cliente = [IDADE]  
– score_credito = 772.4  
– cliente_ativo = True  

Imprima cada variável junto ao tipo de dado correspondente, utilizando a função type().

Obs: Substitua os placeholders com seus dados reais.

## Exercício 3 Operações Aritméticas em Contexto Logístico

Uma empresa de logística quer calcular a quilometragem total e o custo médio de combustível de entregas urbanas. Cada veículo da frota percorre em média [IDADE] quilômetros por dia, e os gastos diários com combustível são equivalentes a [300 + ANO_2_DIGITOS] reais. Para simular esse cálculo, será utilizado um notebook com variáveis fixas, permitindo analisar a operação com diferentes operadores matemáticos: soma, subtração, divisão inteira, porcentagem e resto.

Objetivo  
Calcular e imprimir os resultados de diferentes operações aritméticas a partir de variáveis fixas que simulam consumo e deslocamento logístico.
 
Enunciado  
Defina km_por_dia = [IDADE] e gasto_diario = [ 300 + ANO_2_DIGITOS]. Imprima os resultados de:

Total em uma semana (km_por_dia * 7)  
Diferença entre 100 reais e o gasto diário (100 - gasto_diario)  
Quantos dias o valor de R$500 cobre (500 // gasto_diario)  
Porcentagem do gasto diário em relação a 100 (gasto_diario % 100)  
Média diária de custo por km (gasto_diario / km_por_dia)  
Obs: Substitua os placeholders com seus dados reais. 

Exemplo: IDADE = 23 anos; ANO_2_digitos = 02; 300 + ANO_2_DIGITOS = 302

## Exercício 4 Conversão entre Minutos e Horas

Uma startup de soluções para call centers está desenvolvendo um painel de produtividade que calcula o tempo médio de atendimento por operador. Para testes iniciais, um operador acumulou [150 + ANO_2_DIGITOS] minutos de atendimento em um dia. Já em outro turno, o tempo registrado foi de 2.25 horas. As conversões entre minutos e horas precisam ser feitas diretamente no notebook, sem entrada de dados, garantindo clareza nos resultados para exibição em dashboards internos.

Objetivo

Converter um valor fixo em minutos para horas (com precisão de duas casas decimais) e outro valor de horas para minutos, usando variáveis fixas no notebook.

Enunciado  
Defina as variáveis tempo_minutos = [150 + ANO_2_DIGITOS] e tempo_horas = 2.25.

Calcule quantas horas equivalem a tempo_minutos.  
Calcule quantos minutos equivalem a tempo_horas.  
Imprima os dois resultados.  
Exemplo: IDADE = 23 anos; ANO_2_digitos = 02  

## Exercício 5 Manipulação de Strings com Aspas e Quebras de Linha

Uma equipe de engenharia documental precisa formatar relatórios em texto contendo títulos, aspas e quebras de linha. Em documentos técnicos, é comum representar mensagens com diferentes tipos de aspas, especialmente ao extrair trechos de e-mails ou protocolos. Os dados utilizados incluirão o nome do aluno ([NOME_PROPRIO]) e um título fictício de projeto. Este exercício visa garantir que as strings sejam criadas corretamente mesmo com elementos complexos.

Objetivo  
Definir três strings com aspas simples, duplas e triplas, garantindo que cada uma represente um conteúdo válido e tecnicamente aceitável em relatórios automatizados.

Enunciado

Crie:

Uma string msg_aspas_simples com a frase: Projeto '[NOME_PROPRIO]' em execução.  
Uma string msg_aspas_duplas com a frase: Aluno "[NOME_PROPRIO]" aprovado no teste.  
Uma string relatorio_triple com três linhas de texto (usando aspas triplas), com título, descrição e status final.  
Imprima as três strings exatamente como seriam exibidas em um relatório.  

## Exercício 6 Concatenação de Strings para Mensagem de Boas-Vindas

Uma plataforma de comunicação empresarial deseja testar a geração automática de mensagens com base em dados fixos. Para isso, serão combinadas strings simples como nomes, cargos e identificadores de turma. O nome do aluno [NOME_PROPRIO], seu sobrenome [ULTIMO_SOBRENOME] e o código da turma [CODIGO_CLASSE] serão utilizados para formar uma mensagem de boas-vindas formatada.

Objetivo

Concatenar múltiplas strings com o operador + para compor mensagens estruturadas utilizadas em comunicação interna.

Enunciado  
Defina três variáveis: nome = '[NOME_PROPRIO]', sobrenome = '[ULTIMO_SOBRENOME]' e turma = '[CODIGO_CLASSE]'. Utilize o operador + para criar a string mensagem, no formato:  
"Bem-vindo(a), [NOME] [SOBRENOME]! Sua turma é [CODIGO_CLASSE]."  
Imprima a mensagem final.  

Obs: Substitua os placeholders com seus dados reais. 

## Exercício 7 Repetição de Strings para Alerta Visual

Desenvolvedores de sistemas para testes de impressão precisam simular mensagens repetidas em diversos contextos. Em um dos casos, é necessário imprimir uma mensagem de alerta ou separador visual. Esse alerta usará a string "ATENÇÃO! " repetida para formar uma faixa visual.

Objetivo  
Utilizar o operador * para repetir uma string com fins de destaque visual ou formatação.

Enunciado  
Crie a variável alerta com o valor "ATENÇÃO! ". Crie uma segunda variável faixa_alerta repetindo a string 5 vezes com o operador *. Imprima a faixa completa.

Exercício 8 Transformações de Capitalização em Strings

Uma plataforma de normalização de dados textuais está padronizando nomes, cargos e descrições. Para isso, é essencial que os alunos saibam aplicar transformações como upper(), lower(), title(), capitalize() e outras. A string "[NOME_PROPRIO] [ULTIMO_SOBRENOME]" será usada como base.

Objetivo  
Aplicar funções de capitalização e transformação de strings para padronizar informações de entrada textual.

Enunciado  
Crie uma string nome_completo = '[NOME_PROPRIO] [ULTIMO_SOBRENOME]' e imprima os seguintes resultados:

Tudo em maiúsculo  
Tudo em minúsculo  
Primeira letra de cada nome maiúscula (title())  
Primeira letra da string maiúscula (capitalize())  
Inversão de maiúsculas/minúsculas (swapcase())  
Obs: Substitua os placeholders com seus dados reais.  

## Exercício 9 Verificação de Palavras-Chave com Operador in

Uma ferramenta de filtragem de currículos precisa identificar se palavras-chave estão presentes em perfis de candidatos. Para isso, utiliza-se o operador in para verificar ocorrência de termos. Um exemplo será verificar se a string "Python" aparece em descrições de habilidades como "Domínio em Python, SQL e Excel".

Objetivo  
Testar a ocorrência de uma substring dentro de uma string maior utilizando o operador in.

Enunciado  
Crie uma variável habilidades = 'Domínio em Python, SQL e Excel'. Crie uma segunda variável busca = 'Python'. Verifique se busca está em habilidades e imprima o resultado (True ou False).

## Exercício 10 Contagem de Caracteres e Palavras em Texto 

Uma equipe de análise de reviews automatizados deseja saber quantos caracteres e palavras estão contidos em uma opinião de cliente. Essa informação será usada para definir a exibição dos textos em aplicativos móveis.

Objetivo  
Contar corretamente o número de caracteres e palavras em uma string textual.

Enunciado  
Crie uma variável opiniao = 'Serviço excelente aluno [NOME COMPLETO DO ALUNO], voltarei a comprar!'. Use len() para contar caracteres e count() para contar palavras. Imprima os dois resultados.

Obs: Substitua os placeholders com seus dados reais. 

## Exercício 11 Conversão de String para Inteiro com Operação Matemática

Em sistemas de cadastro de produtos, é comum receber códigos como strings e depois precisar convertê-los para números. Neste teste, a string "2025" deverá ser transformada em inteiro para um cálculo simples.

Objetivo  
Converter dados entre string e inteiro, e realizar operações matemáticas básicas com o resultado convertido.

Enunciado  
Defina ano_txt = '[ANO_NASCIMENTO_4_DIGITOS]'. Converta para inteiro e armazene em ano_int. Some 5 ao valor convertido e imprima o resultado.

Obs: Substitua os placeholders com seus dados reais. 

## Exercício 12 Cálculo de Desconto com Conversão de String

As Óticas SJ90 estão promovendo uma campanha onde o desconto aplicado em óculos é proporcional à idade do cliente. A promoção utiliza um sistema que recebe a idade do comprador como uma string formatada no padrão "[IDADE]" e divide por 3.14 para calcular o percentual de desconto. O valor do produto é fixo: R$599,99. A empresa precisa validar se o sistema está calculando corretamente o valor final com base nessa lógica para cada cliente.

Objetivo

Converter uma string contendo uma expressão matemática em um número decimal, calcular o desconto percentual correspondente e aplicar sobre o valor de R$599,99.

Enunciado

Defina desconto_txt = '[IDADE]'. Avalie a expressão como número decimal e armazene o resultado (dividindo por 3.14) em desconto_num. Calcule o valor de desconto sobre R$599,99 e imprima o valor final a ser pago.