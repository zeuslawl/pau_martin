-- 2.1- Els identificadors de les oficines amb la seva ciutat, els objectius i les vendes reals.

SELECT ciudad, objetivo, ventas
FROM oficinas;

-- 2.2- Els identificadors de les oficines de la regió est amb la seva ciutat, els objectius i les vendes reals.

SELECT region, ciudad, objetivo, ventas
FROM oficinas
WHERE region = 'Este';

-- 2.3- Les ciutats en ordre alfabètic de les oficines de la regió est amb els objectius i les vendes reals.

SELECT region, ciudad, objetivo, ventas
FROM oficinas
ORDER BY ciudad ASC;

-- 2.4- Les ciutats, els objectius i les vendes d'aquelles oficines que les seves vendes superin els seus objectius.

SELECT ciudad, objetivo, ventas
FROM oficinas
WHERE ventas > objetivo;

-- 2.5- Nom, quota i vendes de l'empleat representant de vendes número 107.

SELECT nombre, cuota, ventas
FROM repventas
WHERE num_empl = 107;

-- 2.6- Nom i data de contracte dels representants de vendes amb vendes superiors a 300000.

SELECT nombre, contrato
FROM repventas
WHERE ventas > 300000;

-- 2.7- Nom dels representants de vendes dirigits per l'empleat numero 104 Bob Smith.

SELECT nombre
FROM repventas
WHERE dir = 104;

-- 2.8- Nom dels venedors i data de contracte d'aquells que han estat contractats abans del 1988.

SELECT nombre, contrato
FROM repventas
WHERE contrato < '01-01-1988';

-- 2.9- Identificador de les oficines i ciutat d'aquelles oficines que el seu objectiu és diferent a 800000.

SELECT oficina, ciudad
FROM oficinas
WHERE objetivo != 800000;

-- 2.10- Nom de l'empresa i limit de crèdit del client número 2107.

SELECT empresa, limite_credito
FROM clientes
WHERE num_clie = 2107;

-- 2.11- id_fab com a "Identificador del fabricant", id_producto com a "Identificador del producte" i descripcion com a "descripció" dels productes.

SELECT id_fab AS "Identificador del fabricant", id_producto AS "Identificador del producte", descripcion AS "Descripció"
FROM productos;

-- 2.12- Identificador del fabricant, identificador del producte i descripció del producte d'aquells productes que el seu identificador de fabricant acabi amb la lletra i.

SELECT id_fab, id_producto, descripcion
FROM productos
WHERE id_fab LIKE '%i';

-- 2.13- Nom i identificador dels venedors que estan per sota la quota i tenen vendes inferiors a 300000.

SELECT nombre, num_empl
FROM repventas
WHERE (ventas < quota AND ventas < 300000);

-- 2.14- Identificador i nom dels venedors que treballen a les oficines 11 o 13.

SELECT num_empl, nombre
FROM repventas
WHERE (oficina_rep = 11 OR oficina_rep = 13);

-- 2.15- Identificador, descripció i preu dels productes ordenats del més car al més barat.

SELECT id_producto, descripcion, precio
FROM productos
ORDER BY precio DESC;

-- 2.16- Identificador i descripció de producte amb el valor d'inventari (existencies * preu).

SELECT id_producto, descripcion, (existencias * precio) AS "Valor d'Inventari"
FROM productos;

-- 2.17- Vendes de cada oficina en una sola columna i format amb format "<ciutat> te unes vendes de <vendes>", exemple "Denver te unes vendes de 186042.00".

SELECT (ciudad || ' te unes vendes de ' || ventas
FROM oficinas;

-- 2.18- Codis d'empleats que són directors d'oficines.

SELECT num_empl, nombre
FROM repventas
WHERE num_empl
IN(SELECT dir FROM oficinas WHERE dir = num_empl);

-- 2.19- Identificador i ciutat de les oficines que tinguin ventes per sota el 80% del seu objectiu.

SELECT oficina, ciudad
FROM oficinas
WHERE ventas < (objetivo - (objetivo*20/100));

-- 2.20- Identificador, ciutat i director de les oficines que no siguin dirigides per l'empleat 108.

SELECT oficina, ciudad, dir
FROM oficinas
WHERE dir != 108;

-- 2.21- Identificadors i noms dels venedors amb vendes entre el 80% i el 120% de llur quota.

SELECT num_empl, nombre
FROM repventas
WHERE ventas > (cuota - (cuota*20/100)) AND ventas < (cuota - (cuota*-20)/100);

-- 2.22- Identificador, vendes i ciutat de cada oficina ordenades alfabèticament per regió i, dintre de cada regió ordenades per ciutat.

SELECT num_empl, nombre
FROM repventas
WHERE ventas > (cuota - (cuota*20/100)) AND ventas < (cuota - (cuota*-20)/100);

-- 2.23- Llista d'oficines classificades alfabèticament per regió i, per cada regió, en ordre descendent de rendiment de vendes (vendes-objectiu).

SELECT *, (ventas - objetivo) AS "Rendiment de vendes"
FROM oficinas
ORDER BY region ASC, ventas-objetivo DESC;

-- 2.24- Codi i nom dels tres venedors que tinguin unes vendes superiors.

SELECT num_empl, nombre
FROM repventas
ORDER BY ventas DESC
LIMIT 3;

-- 2.25- Nom i data de contracte dels empleats que les seves vendes siguin superiors a 500000.

SELECT nombre, contrato
FROM repventas
WHERE ventas > 500000;

-- 2.26- Nom i quota actual dels venedors amb el calcul d'una "nova possible quota" que serà la quota de cada venedor augmentada un 3 per cent de les seves propies vendes.

SELECT nombre, cuota
FROM repventas
WHERE ventas > 500000;

-- 2.27- Identificador i nom de les oficines que les seves vendes estan per sota del 80% de l'objectiu.

SELECT oficina, ciudad
FROM oficinas
WHERE ventas < (objetivo - (objetivo*20/100));

-- 2.28- Numero i import de les comandes que el seu import oscil·li entre 20000 i 29999.

SELECT num_pedido, importe
FROM pedidos
WHERE importe > 20000 AND importe < 29999;

-- 2.29- Nom, ventes i quota dels venedors que les seves vendes no estan entre el 80% i el 120% de la seva quota.

SELECT nombre, ventas, cuota 
FROM repventas
WHERE NOT(ventas > (cuota - (cuota*20/100)) AND ventas < (cuota - (cuota*-20)/100));

-- 2.30- Nom de l'empresa i el seu limit de crèdit, de les empreses que el seu nom comença per Smith.

SELECT empresa, limite_credito
FROM clientes
WHERE empresa LIKE 'Smith%';

-- 2.31- Identificador i nom dels venedors que no tenen assignada oficina.

SELECT num_empl, nombre
FROM repventas
WHERE oficina_rep IS NULL;

-- 2.32- Identificador i nom dels venedors, amb l'identificador de l'oficina d'aquells venedors que tenen una oficina assignada.

SELECT num_empl, nombre, oficina_rep
FROM repventas
WHERE oficina_rep IS NOT NULL;

-- 2.33- Identificador i descripció dels productes del fabricant identificat per imm dels quals hi hagin existències superiors o iguals 200, també del fabricant bic amb existències superiors o iguals a 50.

SELECT id_producto, descripcion
FROM productos
WHERE (id_fab = 'imm' AND existencias >= 200) OR (id_fab = 'bic' AND existencias >= 50);

-- 2.34- Identificador i nom dels venedors que treballen a les oficines 11, 12 o 22 i compleixen algun dels següents supòsits:
-- a) han estat contractats a partir de juny del 1988 i no tenen director
-- b) estan per sobre la quota però tenen vendes de 600000 o menors.

SELECT num_empl, nombre
FROM repventas
WHERE (oficina_rep = 11 OR oficina_rep = 12 or oficina_rep = 22) AND ((contrato < '01-06-1988' AND director IS NULL)OR(ventas > cuota AND ventas < 600000));

-- 2.35- Identificador i descripció dels productes amb un preu superior a 1000 i siguin del fabricant amb identificador rei o les existències siguin superiors a 20.



-- 2.36- Identificador del fabricant,identificador i descripció dels productes amb fabricats pels fabricants que tenen una lletra qualsevol, una lletra 'i' i una altre lletra qualsevol com a identificador de fabricant.



-- 2.37- Identificador i descripció dels productes que la seva descripció comenÃ§a per "art" sense tenir en compte les majúscules i minúscules.



-- 2.38- Identificador i nom dels clients que la segona lletra del nom sigui una "a" minúscula o majuscula.



-- 2.39- Identificador i ciutat de les oficines que compleixen algun dels següents supòsits:
-- a) És de la regió est amb unes vendes inferiors a 700000.
-- b) És de la regió oest amb unes vendes inferiors a 600000.



-- 2.40- Identificador del fabricant, identificació i descripció dels productes que compleixen tots els següents supòsits:
-- a) L'identificador del fabricant és "imm" o el preu és menor a 500.
-- b) Les existències són inferiors a 5 o el producte te l'identificador 41003.  

-- 2.41- Identificador de les comandes del fabricant amb identificador "rei" amb una quantitat superior o igual a 10 o amb un import superior o igual a 10000.



-- 2.42- Data de les comandes amb una quantitat superior a 20 i un import superior a 1000 dels clients 2102, 2106 i 2109.


-- 2.43- Identificador dels clients que el seu nom no conté " Corp." o " Inc." amb crèdit major a 30000.



-- 2.44- Identificador dels representants de vendes majors de 40 anys amb vendes inferiors a 400000.


-- 2.45- Identificador dels representants de vendes menors de 35 anys amb vendes superiors a 350000.


