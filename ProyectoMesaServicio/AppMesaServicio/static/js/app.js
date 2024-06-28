function agregarIdCaso(id){
  alert ('hla')
    document.getElementById('idCaso').value=id
  }

// {*}
function mostrarImagen(evento){
  const archivos = evento.target.files
  const archivo = archivos[0]
  const url = URL.createObjectURL(archivo)
  const imagen = document.getElementById('imagenMostrar')
  imagen.setAttribute('src' , url)

}
