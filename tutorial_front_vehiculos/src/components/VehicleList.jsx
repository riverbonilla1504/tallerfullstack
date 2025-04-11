import { useState, useEffect } from "react";
import axios from "axios";
import AddVehicle from "./AddVehicle";
import EditVehicle from "./EditVehicle";

const ListaVehiculos = () => {
    const [vehiculos, setVehiculos] = useState([]);
    const [cargando, setCargando] = useState(true);
    const [error, setError] = useState(null);
    const [mostrarAgregarVehiculo, setMostrarAgregarVehiculo] = useState(false);
    const [mostrarEditarVehiculo, setMostrarEditarVehiculo] = useState(false);
    const [vehiculoSeleccionado, setVehiculoSeleccionado] = useState(null);

    
    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/vehiculos/")
            .then((response) => {
                setVehiculos(response.data.vehiculos);
                console.log(response.data.vehiculos);
                setCargando(false);
            })
            .catch((error) => {
                console.error("Error al obtener los vehículos:", error);
                setError("No se pudieron cargar los vehículos.");
                setCargando(false);
            });
    }, []);

    
    const manejarAgregarVehiculo = (nuevoVehiculo) => {
        setVehiculos((vehiculosPrevios) => [...vehiculosPrevios, nuevoVehiculo]);
    };

    
    const manejarEditarVehiculo = (vehiculoActualizado) => {
        setVehiculos((vehiculosPrevios) =>
            vehiculosPrevios.map((v) => (v.id === vehiculoActualizado.id ? vehiculoActualizado : v))
        );
        setMostrarEditarVehiculo(false);
        setVehiculoSeleccionado(null);
    };

    
    const manejarEliminarVehiculo = (placa) => {
        if (!window.confirm("¿Estás seguro de que deseas eliminar este vehículo?")) return;

        axios
            .delete(`http://127.0.0.1:8000/api/vehiculos/${placa}/`)
            .then(() => {
                setVehiculos((vehiculosPrevios) =>
                    vehiculosPrevios.filter((vehiculo) => vehiculo.placa !== placa)
                );
            })
            .catch((error) => {
                console.error("Error al eliminar el vehículo:", error);
                setError("No se pudo eliminar el vehículo.");
            });
    };

    
    const manejarEditarClick = (vehiculo) => {
        setVehiculoSeleccionado(vehiculo);
        setMostrarEditarVehiculo(true);
    };

    
    const obtenerColor = (color) => {
        const colores = {
            "Azul": "bg-blue-500",
            "Rojo": "bg-red-500",
            "Verde": "bg-green-500",
            "Negro": "bg-gray-800",
            "Blanco": "bg-gray-200 text-gray-800",
            "1": "bg-red-500",
            "2": "bg-blue-500",
            "3": "bg-green-500",
        };
        return colores[color] || "bg-purple-500";
    };

    
    const obtenerNombreColor = (color) => {
        const nombres = {
            "1": "Rojo",
            "2": "Azul",
            "3": "Verde",
        };
        return nombres[color] || "Desconocido";
    };

    if (cargando) return <p className="text-center text-gray-500">Cargando vehículos...</p>;
    if (error) return <p className="text-center text-red-500">{error}</p>;

    return (
        <div className="max-w-4xl mx-auto mt-10 p-5 bg-white shadow-md rounded-lg">
            <h2 className="text-2xl font-bold text-center mb-4 text-blue-600">🐀 Lista de Vehículos</h2>
            <button
                onClick={() => setMostrarAgregarVehiculo(true)}
                className="mb-4 px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700"
            >
                + Agregar vehículo
            </button>

            {vehiculos.length === 0 ? (
                <p className="text-center text-gray-500">No hay vehículos disponibles.</p>
            ) : (
                <ul className="space-y-4">
                    {vehiculos.map((vehiculo) => (
                        <li
                            key={vehiculo.id}
                            className="p-4 border rounded-lg shadow-sm flex items-center justify-between hover:bg-gray-50 transition"
                        >
                            <div>
                                <p className="text-lg font-semibold">
                                    {vehiculo.marca} - {vehiculo.placa}
                                </p>
                                <p className="text-gray-600">Modelo: {vehiculo.modelo}</p>
                            </div>
                            <div className="flex items-center gap-2">
                                <span className={`px-3 py-1 rounded-full text-white ${obtenerColor(vehiculo.color)}`}>
                                    {vehiculo.color}
                                </span>
                                <button
                                    onClick={() => manejarEditarClick(vehiculo)}
                                    className="ml-2 px-3 py-1 bg-yellow-500 text-white rounded hover:bg-yellow-600"
                                >
                                    Editar
                                </button>
                                <button
                                    onClick={() => manejarEliminarVehiculo(vehiculo.placa)}
                                    className="ml-2 px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600"
                                >
                                    Eliminar
                                </button>
                            </div>
                        </li>
                    ))}
                </ul>
            )}

            {mostrarAgregarVehiculo && (
                <AddVehicle
                    onClose={() => setMostrarAgregarVehiculo(false)}
                    onAddVehicle={manejarAgregarVehiculo}
                />
            )}

            {mostrarEditarVehiculo && vehiculoSeleccionado && (
                <EditVehicle
                    vehicle={vehiculoSeleccionado}
                    onClose={() => setMostrarEditarVehiculo(false)}
                    onUpdateVehicle={manejarEditarVehiculo}
                />
            )}
        </div>
    );
};

export default ListaVehiculos;
