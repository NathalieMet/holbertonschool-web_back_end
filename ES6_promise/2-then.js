export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({ status: 200, body: 'Success' }))
    .catch(() => new Error())
    .finally(() => {
      console.log('Got a response from the API');
    });
}

// return promise
// .then((resolve) => {
// ({ status: 200, body: 'Success' });
// })
// .catch(() => {
//  console.error({});
// });
// console.log('Got a response from the API');
// }
