# 🛒 Loja POO

Projeto da disciplina **Programação Orientada a Objetos em Python**.

Durante as aulas, vamos construir **juntos** o "cérebro" de uma loja virtual: produtos, clientes, carrinho de compras, pagamentos e pedidos. Tudo funciona pelo **terminal**.

Cada aluno trabalha na **sua própria cópia** deste repositório (um *fork*) e salva o progresso com **commits**. O histórico de commits mostra o que você fez em cada aula.

> 📘 Login, logout e erros comuns em máquina compartilhada: veja o arquivo `_Orientacoes_e_apoio/Guia-git-github.md`.

---

## 1️⃣ Primeira vez: criar a sua cópia (fork)

1. Entre na sua conta do GitHub pelo navegador.
2. Nesta página, clique no botão **Fork** (canto superior direito) → **Create fork**.
3. Pronto: agora existe `github.com/SEU-USUARIO/loja-turma`. **É nessa cópia que você vai trabalhar.**

## 2️⃣ Primeira vez em cada máquina: baixar o projeto

No VS Code, abra o terminal (**Terminal → Novo Terminal**) e digite um comando por vez. Troque o que está entre aspas pelos seus dados, e `SEU-USUARIO` pelo seu usuário do GitHub:

```powershell
git config --global user.name "Seu Nome Completo"
git config --global user.email "email-da-sua-conta-github@exemplo.com"
cd $HOME\Documents
git clone https://github.com/SEU-USUARIO/loja-turma.git
cd loja-turma
code .
```

## 3️⃣ Executar a loja e rodar os testes

Na janela do VS Code que abriu: **Terminal → Novo Terminal**.

```powershell
py src/main.py
py -m unittest -v
```

- `OK` quer dizer que todos os testes passaram. ✅
- `FAILED` ou `ERROR` quer dizer que ainda falta alguma coisa no código. Leia a mensagem: ela diz qual teste falhou e em qual linha.

## 4️⃣ No começo de cada aula: atualizar

1. No site, abra o **seu** fork (`github.com/SEU-USUARIO/loja-turma`) e clique em **Sync fork → Update branch**. Isso traz os testes novos que a professora colocou.
2. No terminal, dentro da pasta do projeto:
   ```powershell
   git pull
   ```

## 5️⃣ Durante e no fim da aula: commit e push

```powershell
git add .
git commit -m "Aula 3 - cria classes Categoria e Produto"
git push
```

Ou pelo VS Code: **Source Control** (ícone da forquilha) → escreva a mensagem → **Commit** → **Sync Changes**.

Depois, atualize a página do seu fork no site e confira se o commit apareceu.

## 6️⃣ Antes de ir embora: logout

Máquina compartilhada! Siga a seção **"4. Indo embora: logout"** do `Guia-git-github.md`: saia da conta no VS Code, apague nome e e-mail do Git, remova a credencial do Windows e saia do GitHub no navegador.

---

## 📁 O que tem em cada pasta

| Pasta | Para que serve |
|---|---|
| `src/main.py` | Arquivo principal: é ele que a gente executa |
| `src/models/` | As classes da loja (uma classe por arquivo) |
| `tests/` | Testes automáticos. **Não mexa nesta pasta**: só rode os testes |
| `codigo-das-aulas/` | Aparece depois de cada aula: o código pronto, para quem faltou |
| `_Orientacoes_e_apoio/` | Guia de Git e materiais de apoio |

## ⚠️ Combinados

- Escreva o seu código **dentro da pasta `src/`**. Não altere `tests/` nem `codigo-das-aulas/`.
- Faça commit **pelo menos no fim de cada aula**, com uma mensagem que diga o que você fez (ex.: `Aula 4 - cria classe Cliente`).
- Faltou ou perdeu o código? Faça o **Sync fork** e o `git pull`, copie a pasta `src` da última aula que está em `codigo-das-aulas/` para a sua pasta `src`, e faça commit e push.
- **Quem entra, sai:** sempre faça o logout antes de ir embora.
