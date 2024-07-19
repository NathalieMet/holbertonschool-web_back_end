const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const listProducts = [
	{id: 1,
	name: 'Suitcase 250',
	price: 50,
	stock: 0},
	{id: 2,
	name: 'Suitcase 450',
	price: 100,
	stock: 0},
	{id: 3,
	name: 'Suitcase 650',
	price: 350,
	stock: 0},
	{id: 4,
	name: 'Suitcase 1050',
	price: 550,
	stock: 5}
]

const getItemById = (id) => {
	return listProducts.find(product => product.id === id);
  };

const app = express();
const client = redis.createClient();

const reserveStockById = (itemId, stock) => {
	client.set(`item.${itemId}`, stock);
  };

const getAsync = promisify(client.get).bind(client);

const getCurrentReservedStockById = async (itemId) => {
	const stock = await getAsync(`item.${itemId}`);
	return stock ? parseInt(stock, 10) : null;
  };

app.get('/list_products', (req, res) => {
	const products = listProducts.map(product => ({
	  itemId: product.id,
	  itemName: product.name,
	  price: product.price,
	  initialAvailableQuantity: product.stock,
	}));
	res.json(products);
  });

app.get('/list_products/:itemId', async (req, res) => {
	const itemId = parseInt(req.params.itemId, 10);
	const product = getItemById(itemId);
	if (!product) {
	  return res.json({ status: 'Product not found' });
	}
	const currentStock = await getCurrentReservedStockById(itemId);
	const currentQuantity = currentStock !== null ? currentStock : product.stock;
	res.json({
	  itemId: product.id,
	  itemName: product.name,
	  price: product.price,
	  initialAvailableQuantity: product.stock,
	  currentQuantity: currentQuantity,
	});
  });

app.get('/reserve_product/:itemId', async (req, res) => {
	const itemId = parseInt(req.params.itemId, 10);
	const product = getItemById(itemId);
	if (!product) {
	  return res.json({ status: 'Product not found' });
	}
	const currentStock = await getCurrentReservedStockById(itemId);
	const currentQuantity = currentStock !== null ? product.stock - currentStock : product.stock;

	if (currentQuantity <= 0) {
	  return res.json({ status: 'Not enough stock available', itemId: itemId });
	}

	reserveStockById(itemId, currentStock + 1);
	res.json({ status: 'Reservation confirmed', itemId: itemId });
  });

if (require.main === module) {
	const PORT = 1245;
	app.listen(PORT, () => {
	  console.log(`API available on localhost port ${PORT}`);
	});
  }

module.exports = app;
