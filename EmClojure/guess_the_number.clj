; guess_the_number.clj

(ns guess-the-number.core
  (:gen-class))

;; --- Lógica Pura ---

(defn checar-palpite
  "Compara o palpite com o número secreto. Função pura."
  [numero-secreto palpite]
  (cond
    (< palpite numero-secreto) :muito-baixo
    (> palpite numero-secreto) :muito-alto
    :else :correto))

;; --- Funções Impuras (I/O) e o Loop ---

(defn exibir-mensagem
  "Função impura para mostrar mensagens ao usuário."
  [resultado tentativas]
  (let [mensagens {:muito-baixo "Muito baixo!"
                   :muito-alto  "Muito alto!"
                   :correto     "Parabéns, você acertou!"}]
    (println (get mensagens resultado)))
  (when (and (not= resultado :correto) (> tentativas 0))
    (println (str "Você tem " tentativas " tentativas restantes."))))

(defn pedir-palpite-usuario
  "Função impura para obter input do usuário."
  []
  (println "Digite seu palpite: ")
  (try
    (Integer/parseInt (read-line))
    (catch NumberFormatException e
      (println "Por favor, digite um número válido.")
      (pedir-palpite-usuario)))) ; Chama a si mesmo em caso de erro

(defn loop-do-jogo
  "O loop principal do jogo, usando loop/recur para recursão otimizada."
  [estado]
  (if (:fim-de-jogo estado)
    ; Condição de parada
    (if (> (:tentativas-restantes estado) 0)
        (println "Você venceu!")
        (println (str "Fim de jogo! O número era " (:numero-secreto estado))))
    ; Corpo do loop
    (let [palpite   (pedir-palpite-usuario)
          resultado (checar-palpite (:numero-secreto estado) palpite)
          
          ; Atualiza o estado de forma imutável
          tentativas-atualizadas (- (:tentativas-restantes estado) 1)
          fim-de-jogo? (or (= resultado :correto) (<= tentativas-atualizadas 0))
          proximo-estado (assoc estado 
                                :tentativas-restantes tentativas-atualizadas
                                :fim-de-jogo fim-de-jogo?)]
      
      (exibir-mensagem resultado (:tentativas-restantes proximo-estado))
      (recur proximo-estado)))) ; Recur: chama o loop novamente com o novo estado

;; --- Ponto de Entrada do Programa ---

(defn -main
  "Função principal que inicia o jogo."
  []
  (println "--- Adivinhe o Número (de 1 a 100) ---")
  (let [numero-secreto (inc (rand-int 100)) ; inc para ir de 1-100
        estado-inicial {:numero-secreto numero-secreto
                        :tentativas-restantes 7
                        :fim-de-jogo false}]
    (loop-do-jogo estado-inicial)))
