function DeleteCategoria()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_categoria").setAttribute("href","/eliminar/"+id)
    })
}
function DeleteIngreso()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_categoria").setAttribute("href","/eliminar-ingreso/"+id)
    })
}
function DeleteProducto()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_categoria").setAttribute("href","/eliminar-producto/"+id)
    })
}
function DeleteProveedor()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_categoria").setAttribute("href","/eliminar-proveedor/"+id)
    })
}
function DeleteSalida()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_categoria").setAttribute("href","/eliminar-salida/"+id)
    })
}

function DeleteEmpleado()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_categoria").setAttribute("href","/eliminar-empleado/"+id)
    })
}

function DeleteUser()
{
    var modal = document.getElementById("deleteModal")
    modal.addEventListener('show.bs.modal',function(event){
        var button = event.relatedTarget
        var name = button.getAttribute("data-bs-name")
        var id = button.getAttribute("data-bs-id")
        modal.querySelector(".modal-title span").innerHTML=name
        modal.querySelector("#eliminar_categoria").setAttribute("href","/eliminar-usuario/"+id)
    })
}