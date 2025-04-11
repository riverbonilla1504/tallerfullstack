import { useState } from "react";
import axios from "axios";

const EditVehicle = ({ vehicle, onClose, onUpdateVehicle }) => {
  const [formData, setFormData] = useState({
    placa: vehicle.placa,
    marca: vehicle.marca,
    modelo: vehicle.modelo,
    color: vehicle.color,
  });

  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const validateForm = () => {
    let newErrors = {};
    if (formData.placa.length > 6) newErrors.placa = "Máximo 6 caracteres";
    if (formData.marca.length > 10) newErrors.marca = "Máximo 10 caracteres";
    if (formData.modelo <= 0 || isNaN(formData.modelo)) newErrors.modelo = "Debe ser un número positivo";

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;

    try {
      await axios.put(`${import.meta.env.VITE_API_URL}/vehiculo/actualizar/${vehicle.id}`, formData);
      onUpdateVehicle(formData);
      onClose();
    } catch (error) {
      console.error("Error al actualizar el vehículo:", error);
    }
  };

  return (
    <div className="fixed inset-0 flex items-center justify-center bg-gray-900 bg-opacity-50">
      <div className="bg-white p-6 rounded-lg shadow-lg w-96">
        <h2 className="text-2xl font-bold text-center text-blue-600 mb-4">✏️ Editar Vehículo</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700">Placa</label>
            <input
              type="text"
              name="placa"
              value={formData.placa}
              onChange={handleChange}
              className="w-full p-2 border rounded"
            />
            {errors.placa && <p className="text-red-500 text-sm">{errors.placa}</p>}
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700">Marca</label>
            <input
              type="text"
              name="marca"
              value={formData.marca}
              onChange={handleChange}
              className="w-full p-2 border rounded"
            />
            {errors.marca && <p className="text-red-500 text-sm">{errors.marca}</p>}
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700">Modelo</label>
            <input
              type="number"
              name="modelo"
              value={formData.modelo}
              onChange={handleChange}
              className="w-full p-2 border rounded"
            />
            {errors.modelo && <p className="text-red-500 text-sm">{errors.modelo}</p>}
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700">Color</label>
            <select
              name="color"
              value={formData.color}
              onChange={handleChange}
              className="w-full p-2 border rounded"
            >
              <option value="">Selecciona un color</option>
              <option value="rojo">Rojo</option>
              <option value="azul">Azul</option>
              <option value="verde">Verde</option>
              <option value="negro">Negro</option>
              <option value="blanco">Blanco</option>
              <option value="gris">Gris</option>
            </select>
          </div>

          <div className="flex justify-end space-x-2">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 bg-gray-300 text-gray-800 rounded hover:bg-gray-400"
            >
              Cancelar
            </button>
            <button
              type="submit"
              className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
            >
              Guardar
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default EditVehicle;
