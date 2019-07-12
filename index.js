const onLoad = () => {
  console.log("I'm working !!");

  const h1 = document.querySelector('h1');
  h1.style.cursor = 'pointer';
  h1.style.addEventListener(
    'click',
    (event)=> {
      console.log (event);
      h1.style.color = 'purple';
    });


}
window.addEventListener("load" , onLoad);
