var lista_de_elems, elem_encontrado;
function found_elem_by_text(tag,texto){
    lista_de_elems = document.getElementsByTagName(tag);
    for (let i = 0; i < lista_de_elems.length; i++) {
      if (lista_de_elems[i].textContent == texto) {
        elem_encontrado = lista_de_elems[i];
        break;
      }
    }
    return elem_encontrado
}
found_elem_by_text("span","Login")