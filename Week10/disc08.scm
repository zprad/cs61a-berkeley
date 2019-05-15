(define (concat a b)
    (if (equal? a nil)
        b
        (cons (car a) (concat (cdr a) b))))

(define (replicate x n)
    (if (= n 0)
        nil
        (cons x (replicate x (- n 1)))))

(define (uncompress s)
    (if (equal? s nil)
        nil
        (concat (replicate (car (car s))
                           (car (cdr (car s))))
                (uncompress (cdr s)))))

(define (map fn lst)
    (if (equal? lst nil)
        lst
        (cons (fn (car lst))
              (map fn (cdr lst)))))

// todo
(define (deep-map fn lst)
    )

(define (make-tree label branches) (cons label branches))

(define (label tree) (car tree))

(define (branches tree) (cdr tree))



