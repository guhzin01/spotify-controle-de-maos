# 🎮 Spotify Hand Control

## 📌 Sobre o projeto

Este é um projeto pessoal desenvolvido com o objetivo de aplicar e aprofundar conhecimentos em visão computacional utilizando Python.

A proposta é criar um sistema capaz de reconhecer gestos com as mãos, capturados pela webcam, e utilizá-los para interagir com o Spotify, permitindo controlar ações como play, pause, troca de músicas e volume sem o uso de teclado ou mouse.

---

## 🎯 Objetivo

O principal objetivo deste projeto é:

* Praticar visão computacional na prática
* Trabalhar com detecção de mãos em tempo real
* Explorar interação entre usuário e sistema através de gestos
* Evoluir habilidades em Python e bibliotecas como MediaPipe e OpenCV

---

## 🧠 Tecnologias utilizadas

* Python
* OpenCV
* MediaPipe

---

## ⚙️ Funcionalidades atuais

* Captura de vídeo em tempo real via webcam
* Detecção de mãos utilizando MediaPipe
* Identificação de landmarks (21 pontos da mão)
* Visualização dos pontos na tela

---

## 🚧 Funcionalidades futuras

* Controle de play/pause com gestos
* Troca de música com movimentos da mão
* Controle de volume por distância entre dedos
* Integração com a API do Spotify

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/guhzin01/spotify-controle-de-maos.git
```

2. Acesse a pasta do projeto:

```bash
cd spotify-controle-de-maos
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o projeto:

```bash
python hand_test.py
```

---

## 📁 Estrutura do projeto

* `hand_test.py` → Detecção de mãos
* `camera_test.py` → Teste da webcam
* `gestos.py` → Lógica de gestos (em desenvolvimento)
* `models/` → Modelo utilizado pelo MediaPipe

---

## 💡 Considerações

Este projeto está em desenvolvimento e faz parte do meu processo de aprendizado prático em programação e desenvolvimento de sistemas interativos.
