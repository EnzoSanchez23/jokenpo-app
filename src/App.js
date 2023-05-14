function JogadaBOT() {
  const jogadas = ['Pedra', 'Papel', 'Tesoura'];
  var bot = jogadas[Math.floor(Math.random() * jogadas.length)]
  console.log("Jogada do BOT:" + bot);
  return bot;
}

function jogadaPlayer(jogada){
  const bot = JogadaBOT();

  if(jogada === bot){
    console.log("Empate");
  }

  else if( (jogada === "Pedra" && bot === "Tesoura") || (jogada === "Papel" && bot === "Pedra") || (jogada === "Tesoura" && bot === "Papel")){
    console.log("Vitoria do Jogador");
  }
  else{
    console.log("Vitoria do BOT");
  }

}

function App() {
  return (
    <div>
      <button onClick={()=>jogadaPlayer("Pedra")} >Pedra</button>
      <button onClick={()=>jogadaPlayer("Papel")} >Papel</button>
      <button onClick={()=>jogadaPlayer("Tesoura")} >Tesoura</button>
    </div>
  );
}

export default App;
