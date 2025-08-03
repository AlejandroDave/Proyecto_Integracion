import { ReactNode } from "react";

/*
Los componentes son complementos reutilizables que facilitaran el diseño de la interfaz, dichos complementos se
conforman por una funcion la cual puede ser dividida en distintas funciones dependiendo el uso que se les de.

*/
interface CardProps {
  //Se instancia una interface previa que indicara el tipo de valor que esta funcion estara recibiendo
  children: ReactNode;
}
function Card(props: CardProps) {
  // Al tener la interface definida se le indicara que el parametro sera de ese tipo

  const { children } = props; // Se declara una variable que recibira el valor del parametro

  return (
    <div className="card" style={{ width: "750px", background: "white" }}>
      <div className="card-body">{children}</div>
    </div>
  );
}

interface CardBodyProps {
  title: string;
  secondtitle?: string;
  text?: string;
}

export function CardBody(props: CardBodyProps) {
  const { title, secondtitle, text } = props;

  return (
    <>
      <h5 className="card-title">{title}</h5>
      <h6 className="card-subtitle mb-2 text-body-secondary">{secondtitle}</h6>
      <p className="card-text">{text}</p>
    </>
  );
}

export default Card;

interface Headerprops {
  head: string;
  title: string;
  text?: string;
}

export function CabeceraCard(props: Headerprops) {
  const { head, title, text } = props;
  return (
    <div className="card">
      <div className="card-body">
        <h5 className="card-title">Estoy aprendiendon {head}</h5>
        <p className="card-text"> a traves de un curso en {title}</p>
        <a
          href="https://www.youtube.com/watch?v=yIr_1CasXkM&t=3466s"
          className="btn btn-primary"
        >
          Ir al curso
        </a>
      </div>
    </div>
  );
}
