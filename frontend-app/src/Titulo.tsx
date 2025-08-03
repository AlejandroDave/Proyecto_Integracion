import { ReactNode } from "react";

interface Titleprops{
    children: ReactNode;

}

function Titulo({ children }: Titleprops){
    
    return  <h1>{ children }</h1>;
}

export default Titulo   // Exporta por defecto la aplicacion con nombre App

interface datosTitulo{
    nombre: string;
    apellido?: string;

}

export function TituloBody(props: datosTitulo){
        const {nombre, apellido}=  props;
        return(<p className="card-text">Hola {nombre} {apellido}</p>);

}