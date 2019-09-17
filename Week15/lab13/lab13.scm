; Lab 13: Final Review

; Q3
(define (compose-all funcs)
  (define (compose-all-with func_list init)
    (if (null? func_list)
        init
        (compose-all-with (cdr func_list) ((car func_list) init))
        ))
  (lambda (x) (compose-all-with funcs x))
)