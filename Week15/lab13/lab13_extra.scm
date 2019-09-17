; Lab 13: Final Review - Optional Questions

; Q6
(define (nodots s)
  (cond ((null? s) nil)
        ((not (pair? s)) (cons s nil))
        ((pair? (car s)) (cons (nodots (car s)) (nodots (cdr s))))
        (else (cons (car s) (nodots (cdr s)))))
)

; (define (concat-list s l)
;   (cond ((null? s) l)
;     (else (cons (car s) (concat-list (cdr s) l)))))

; Q7
(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond ((null? curr) #f)
          ((contains? seen-so-far curr) #t)
          (else (pair-tracker (cons curr seen-so-far) (cdr-stream curr))))
    )
  (pair-tracker nil s)
)

(define (contains? lst s)
  (cond ((null? lst) #f)
        ((eq? (car lst) s) #t)
        (else (contains? (cdr lst) s)))
)

; Q8
(define-macro (switch expr cases)
    (let ((val (eval expr)))
      (cons 'cond
            (map (lambda (case)
                         (cons (eq? val (car case)) (cdr case))
                 )
                 cases)))
)