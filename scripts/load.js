import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  stages : [
    { duration: '120s', target: 20 },
    { duration: '180s', target: 50 },
    { duration: '120s', target: 10 }
  ]

};

export default function() {
  http.get('http://localhost:9898');
  sleep(1);
}
