import React, { useState } from "react";

type Props = {
    data: string[];
    onSelect?: (elemento: string) => void;

};

function List({ data, onSelect }: Props){
    
    const [index, setIndex] = useState(0); //La funcion Use state nos permite devolver el valor de un estado dentro del codigo
    const handleClick= (i:number, elemento: string) => {
                    setIndex(i);  // se cambia el valor del indice al valor activado
                    onSelect?.(elemento);
                } 

    return (<ul className="list-group" style={{width: "310px"}}>
                {data.map((elemento, i) => (
                    <li onClick={()=> handleClick(i, elemento)} 
                        key={elemento} 
                        className={`list-group-item ${index==i? 'active': ""}`}>{elemento}</li>))}
            </ul>
);
/*
    Lo que se hace en este codigo es mostrar una lista de elementos de n valores que se mostraran acorde al arreglo que se le
    pase, posteriormente mostrara como activado a la opcion clickeada con la funcion handleClick que modificara el valor del
    indice de useState, posteriormente se condicionara que si se tiene el valor del indice y de la opcion seleccionada igual
    esta se mostrara activada.
    Esto es util para mostrar componentes seleccionados en la pagina. 

*/
}


export default List;